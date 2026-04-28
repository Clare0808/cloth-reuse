<template>
  <div class="ele">
    <div class="user-choose-box">
      <div v-for="(index, user) in userList" :key="index">
        <div class="user">
          <div class="user-inframe">
            <div class="name">{{ user.name }}</div>
            <div class="last-time"></div>
          </div>
          <div class="msg"></div>
        </div>
      </div>
    </div>
    <div class="chat-box-outframe">
      <div class="title">aaa</div>
      <div class="chat-box" ref="chatContainer">
        <div v-for="(msg, index) in allMessages" :key="index">
          <div class="chat-sender-box" v-if="msg.fromSender">
            <div class="time">{{ msg.time }}</div>
            <div class="chat-ele">{{ msg.message }}</div>
          </div>
          <div class="chat-receiver-box" v-else>
            <div class="chat-ele">{{ msg.message }}</div>
            <div class="time">{{ msg.time }}</div>
          </div>
        </div>
      </div>
      <div class="input-frame">
        <input type="text" v-model.trim="inputMsg" />
        <div class="send-btn" @click="AddMessages">
          <i class="fa-solid fa-paper-plane"></i>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, watch, nextTick, onMounted } from "vue";

import { chatUiStore } from "@/store/chat";
import { loginUiStore } from "@/store/login";

import { io } from "socket.io-client";

export default {
  setup() {
    const chatStore = chatUiStore();
    const loginStore = loginUiStore();

    const inputMsg = ref("");
    const userEmail = ref("");
    const chatContainer = ref(null);
    const allMessages = ref([]);
    const userList = ref([]);

    // 生成聊天室識別碼
    const getRoomId = (id1, id2) => {
      const sortedIds = [id1, id2].sort(); // 確保順序一致
      return `${sortedIds[0]}-${sortedIds[1]}`;
    };

    // 添加訊息
    const AddMessages = () => {
      // 取得現在時間並格式化
      const formattedTime = new Intl.DateTimeFormat("zh-TW", {
        hour: "numeric",
        minute: "numeric",
        hour12: true,
        timeZone: "Asia/Taipei",
      })
        .format(new Date())
        .replace("AM", "上午")
        .replace("PM", "下午");

      allMessages.value.push({
        fromSender: true,
        message: inputMsg.value,
        time: formattedTime,
      });

      SendMessage();

      inputMsg.value = ""; // 清空輸入框

      // 有新訊息自動滾動到底部
      nextTick(() => {
        if (chatContainer.value) {
          chatContainer.value.scrollTop = chatContainer.value.scrollHeight;
        }
      });
    };

    // 建立 WebSocket 連線
    const socket = io("http://localhost:5000", {
      transports: ["websocket"],
    });

    socket.on("connect", () => {
      console.log("WebSocket 連線成功！");

      const roomId = getRoomId(userEmail.value, chatStore.chatReceiverEmail);

      socket.emit("join_room", { room: roomId }); // 讓使用者加入聊天室
    });

    socket.on("connect_error", (err) => {
      console.error("WebSocket 連線失敗！", err);
    });

    // 發送訊息給其他用戶
    const SendMessage = () => {
      const latestMsg = inputMsg.value.trim();
      const latestTime = new Date();
      const roomId = getRoomId(userEmail.value, chatStore.chatReceiverEmail);

      // 發送訊息到 WebSocket 伺服器
      socket.emit("new_msg", {
        sender_email: userEmail.value,
        receiver_email: chatStore.chatReceiverEmail,
        message: latestMsg,
        time: latestTime,
        room: roomId,
      });
    };

    // 取得聊天紀錄
    const FetchHistory = async () => {
      try {
        // 根據ID取得聊天歷史紀錄
        const response = await fetch(
          `http://localhost:5000/api/chat-history?sender_email=${userEmail.value}&receiver_email=${chatStore.chatReceiverEmail}`
        );
        const history = await response.json();

        console.log("history:", history);

        allMessages.value = history.map((msg) => {
          const isSender = String(msg.sender_email) === String(userEmail.value); // 判斷訊息是否是自己發送的

          const formattedTime = new Intl.DateTimeFormat("zh-TW", {
            hour: "numeric",
            minute: "numeric",
            hour12: true,
            timeZone: "Asia/Taipei",
          })
            .format(new Date(msg.timestamp))
            .replace("AM", "上午")
            .replace("PM", "下午");

          return {
            fromSender: isSender,
            message: msg.message,
            time: formattedTime,
          };
        });
      } catch (error) {
        console.error("獲取歷史訊息失敗:", error);
      }
    };

    const GetSenderList = async () => {
      const response = await fetch("http://localhost:5000/api/all-chat");
      const data = await response.json();

      const filteredData = data.filter((item) => {
        return item.receiver_email === userEmail.value;
      });

      const userData = await loginStore.getUserInfo();

      userList.value = filteredData.map((item) => {
        return {
          item,
          name: userData.find((user) => user.email === item.sender_email).name,
        };
      });

      console.log(userList.value);
    };

    watch(
      () => chatStore.chatReceiverEmail,
      async () => {
        await FetchHistory();

        nextTick(() => {
          if (chatContainer.value) {
            chatContainer.value.scrollTop = chatContainer.value.scrollHeight;
          }
        });
      }
    );

    onMounted(async () => {
      userEmail.value = localStorage.getItem("userEmail");

      const roomId = getRoomId(userEmail.value, chatStore.chatReceiverEmail);
      socket.emit("join_room", {
        room: roomId,
      }); // 讓使用者加入聊天室

      // 先移除所有舊的監聽，避免累積事件
      socket.off("new_msg");

      // 監聽訊息
      socket.on("new_msg", (data) => {
        if (String(data.sender_email) !== String(userEmail.value)) {
          allMessages.value.push({
            fromSender: false,
            message: data.message,
            time: data.time,
          });
          nextTick(() => {
            if (chatContainer.value)
              chatContainer.value.scrollTop = chatContainer.value.scrollHeight;
          });
        }
      });

      await FetchHistory();

      nextTick(() => {
        if (chatContainer.value) {
          chatContainer.value.scrollTop = chatContainer.value.scrollHeight;
        }
      });

      socket.emit("join_room", { user_id: userEmail.value });

      //   await FetchHistory(userEmail.value, chatStore.chatReceiverEmail);

      // 有新訊息自動滾動到底部
      nextTick(() => {
        if (chatContainer.value) {
          chatContainer.value.scrollTop = chatContainer.value.scrollHeight;
        }
      });

      await GetSenderList();
    });

    return {
      chatStore,
      inputMsg,
      userEmail,
      chatContainer,
      allMessages,
      userList,
      AddMessages,
      SendMessage,
      FetchHistory,
      GetSenderList,
    };
  },
};
</script>

<style scoped>
.ele {
  width: calc(55% - 40px);
  height: calc(95% - 40px);
  background-color: #d3dcba;
  border-radius: 12px;
  border: 1px solid #3b5131;
  padding: 20px;
  display: grid;
  grid-template-columns: 45% 55%;
  justify-content: start;
  align-items: start;
}
.user-choose-box {
  width: calc(100% - 20px);
  max-height: 580px;
  overflow-y: auto;
  padding-right: 20px;
}
.user {
  width: calc(100% - 20px);
  height: 50px;
  color: #3b5131;
  background-color: #ffffff;
  font-size: 22px;
  border-radius: 6px;
  text-align: left;
  margin: 10px 0;
  padding: 10px;
}
.user-inframe {
  margin-bottom: 5px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.last-time,
.msg {
  color: #adadad;
  font-size: 18px;
}
.chat-box-outframe {
  width: calc(100% - 40px);
  height: calc(90% - 50px);
  padding: 20px;
}
.title {
  width: 100%;
  color: #3b5131;
  font-size: 24px;
  font-weight: bold;
  border-bottom: 2px solid #3b5131;
  padding-bottom: 5px;
}
.chat-box {
  width: calc(100% - 20px);
  height: 100%;
  background-color: #ffffff;
  padding: 0 10px;
}
.chat-sender-box,
.chat-receiver-box {
  width: 100%;
  min-height: 30px;
  font-size: 20px;
  text-align: left;
  line-height: 30px;
  margin: 15px 0;
  display: flex;
  align-items: center;
}
.chat-sender-box {
  justify-content: end;
}
.chat-sender-box .chat-ele {
  max-width: 85%;
  border: 1px solid #3b5131;
  border-radius: 8px;
  padding: 5px;
}
.chat-receiver-box {
  justify-content: start;
}
.chat-receiver-box .chat-ele {
  max-width: 85%;
  background-color: #d3dcba;
  border-radius: 8px;
  padding: 5px;
}
.time {
  font-size: 16px;
  color: #adadad;
  margin: 0 10px;
}
.input-frame {
  width: 100%;
  padding: 10px;
  display: flex;
  justify-content: center;
  align-items: center;
}
input {
  width: 85%;
  height: 30px;
  font-family: "Pacifico", cursive;
  border: 1px solid #849c7d;
  border-radius: 12px;
  margin-right: 10px;
  padding-left: 10px;
}
input:focus {
  outline: none;
  border-color: #3b5131;
}
.send-btn {
  color: #3b5131;
  line-height: 25px;
  transition: all 0.3s ease;
}
.send-btn:hover {
  color: #ffffff;
  cursor: pointer;
  transform: scale(1.05);
}
</style>
