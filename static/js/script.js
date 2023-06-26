// Example POST method implementation:
async function postData(url = "", data = {}) {
  const response = await fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  });
  return response.json();
}

const questionInput = document.getElementById("questionInput");
const sendButton = document.getElementById("sendButton");

sendButton.addEventListener("click", async () => {
  const questionValue = questionInput.value;
  questionInput.value = "";
  document.querySelector(".right2").style.display = "block";
  document.querySelector(".right1").style.display = "none";
  question1.innerHTML = questionValue;
  question2.innerHTML = questionValue;
  let result = await postData("/api", { question: questionValue });
  solution.innerHTML = result.answer;
});

questionInput.addEventListener("keydown", (event) => {
  if (event.key === "Enter") {
    sendButton.click();
  }
});
