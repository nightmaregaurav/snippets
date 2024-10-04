export const passSsoToken = (
  callback: (ssoUrl: string) => void,
  errorCallback?: (ssoUrl: string, error: string) => void
) => {
  const ssoUrl = '';
  const ssoEndpoint = '/sso-receiver';

  const ssoToken = localStorage.getItem('sso-token');

  let existingFrame = document.getElementById("sso-frame");
  if (existingFrame) {
    existingFrame.remove();
  }

  const ssoFrame = document.createElement("iframe");
  ssoFrame.setAttribute("frameborder", "0");
  ssoFrame.setAttribute("width", "0px");
  ssoFrame.setAttribute("height", "0px");
  ssoFrame.setAttribute("id", "sso-frame");
  ssoFrame.setAttribute("src", `${ssoUrl}${ssoEndpoint}`);
  document.body.appendChild(ssoFrame);

  let newSsoFrame = document.getElementById("sso-frame") as HTMLIFrameElement;

  window.addEventListener(
    "message",
    (event) => {
      if(event && event.data && event.data.eventType === "sso-login-success") {
        console.log("SSO login success acknowledged by SSO sender!");
        callback(ssoUrl);
      }

      if(event && event.data && event.data.eventType === "sso-login-failure") {
        console.log("SSO login failure acknowledged by SSO sender!");
        errorCallback && errorCallback(ssoUrl, event.data.payload.error);
      }
    },
    {
      once: true
    }
  );

  newSsoFrame.onload = () => {
    console.log("SSO frame loaded! Sending SSO token to SSO receiver...");
    newSsoFrame.contentWindow.postMessage(
      {
        eventType: "sso-login",
        payload: { ssoToken }
      },
      ssoUrl
    );
  }
}
