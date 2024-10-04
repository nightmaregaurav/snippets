import React from "react";

const saveTokenAndAcknowledge = (handle, token, senderOrigin) => {
  const storage = handle?.localStorage ?? localStorage;
  storage.setItem("sso-token", token);
  parent.postMessage(
    {
      eventType: "sso-login-success",
    },
    senderOrigin
  );
};

const handleSsoLogin = (senderOrigin, token) => {
  if (!document?.requestStorageAccess){
    saveTokenAndAcknowledge(null, token, senderOrigin);
    return;
  }

  document.requestStorageAccess({ localStorage: true }).then(
    (handle) => {
      saveTokenAndAcknowledge(handle, token, senderOrigin);
    },
    () => {
      parent.postMessage(
        {
          eventType: "sso-login-failure",
          payload: {
            error: "Could not automatically log you in to new portal."
          }
        },
        senderOrigin
      );
    }
  );
};

global.window && window.addEventListener(
  "message",
  (event) => {
    if(event?.data?.eventType === "sso-login") {
      console.log("SSO login token received! Sending success message to sender...");
      const senderOrigin = event.origin;
      const token = event.data.payload.ssoToken
      handleSsoLogin(senderOrigin, token);
    }
  },
  {
    once: true
  }
);

export default function Page() {
  return (<span>Loading...</span>);
}
