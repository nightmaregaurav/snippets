const sgMail = require('@sendgrid/mail')
// const ApiKey = "";
sgMail.setApiKey(ApiKey)

const msg = {
  to: '',
  cc: '',
  from: '',
  subject: 'Sending with SendGrid is Fun',
  text: 'and easy to do anywhere, even with Node.js',
  html: '<strong>and easy to do anywhere, even with Node.js</strong>',
}

sgMail
  .send(msg)
  .then((response) => {
    console.log(response[0].statusCode)
    console.log(response[0].headers)
  })
  .catch((error) => {
    console.error(error)
    console.error(error.response.body.errors)
  });
