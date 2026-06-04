export const reloadAppPage = () => {
  if (window.location.pathname.startsWith("/static")) {
    window.location.replace("/");
    return;
  }

  window.location.reload();
};
