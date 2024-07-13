const sgMail = require('@sendgrid/mail');

const API_KEY = "";
const TEMPLATE_ID = "";
const DATA = {
  ResetPasswordUrl: '',
};

sendEmail(
  'to@gmail.com',
  'from@xyz.com',
  'subject',
  DATA
);

async function sendEmail(to, from, subject, dynamicTemplateData){
  sgMail.setApiKey(API_KEY);
  try {
    const msg = {
      to: to,
      from: from,
      subject: subject,
      templateId: TEMPLATE_ID,
      dynamic_template_data: dynamicTemplateData,
    };

    await sgMail.send(msg);
    console.log('Email sent successfully');
  } catch (error) {
    console.error('Error sending email:', error);
    if (error.response) {
      console.error(error.response.body);
    }
  }
};
