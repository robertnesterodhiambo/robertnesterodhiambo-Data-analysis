function myFunction1() {
  const doc = DocumentApp.create('Tester 1');
}

function myFunction2(){
  const doc1 = DocumentApp.create('Test 2');
  const body = doc1.getBody();
  Logger.log(body);
  body.appendParagraph("Hello Naruto");
}

function myFunction3(){
  const id = '17cs6__YjeMF47HeVmTLtl_XMh9DYVpg4fF5BqrNIL1I';
  const doc = DocumentApp.openById(id);
  const body = doc.getBody();
  const para = body.appendParagraph('HELLO NARUTO');
  Logger.log(doc);
}

function myFunction4(){
  const id = '17cs6__YjeMF47HeVmTLtl_XMh9DYVpg4fF5BqrNIL1I';
  const doc = DocumentApp.openById(id);
  const body = doc.getBody();
  const para = body.appendParagraph("HELLO THIS IS KAKAROT")
  doc.getName()
}

function sendigemail(){
  const email = Session.getActiveUser().getEmail();
  Logger.log(email);
  const id = '17cs6__YjeMF47HeVmTLtl_XMh9DYVpg4fF5BqrNIL1I';
  const doc = DocumentApp.openById(id);
  const body = doc.getBody();
  let emailcontent = body.editAsText().getText();
  const subject = doc.getName();
  const url = doc.getUrl();
  emailcontent += " " + url;
  GmailApp.sendEmail(email,subject,emailcontent);
}
