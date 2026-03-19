const apiStatus = document.getElementById("apiStatus");
const commentInput = document.getElementById("commentInput");
const analyzeBtn = document.getElementById("analyzeBtn");
const clearBtn = document.getElementById("clearBtn");
const errorBox = document.getElementById("errorBox");
const resultCard = document.getElementById("resultCard");
const resultLabel = document.getElementById("resultLabel");
const resultReason = document.getElementById("resultReason");
const traceBox = document.getElementById("traceBox");

function setApiStatus(ok) {
  apiStatus.classList.remove("pending", "ok", "down");
  if (ok) {
    apiStatus.classList.add("ok");
    apiStatus.textContent = "API online";
    return;
  }
  apiStatus.classList.add("down");
  apiStatus.textContent = "API unreachable";
}

function setBusy(isBusy) {
  analyzeBtn.disabled = isBusy;
  analyzeBtn.textContent = isBusy ? "Analyzing..." : "Analyze Comment";
}

function showError(message) {
  errorBox.textContent = message;
  errorBox.classList.remove("hidden");
}

function clearError() {
  errorBox.classList.add("hidden");
  errorBox.textContent = "";
}

function renderResult(payload) {
  const label = String(payload.label || "unknown").toLowerCase();
  resultLabel.textContent = label;
  resultLabel.className = `pill ${label}`;
  resultReason.textContent = payload.reason || "No reason returned.";
  resultCard.classList.remove("hidden");
}

function updateTrace(requestPayload, responsePayload, statusCode) {
  const requestText = JSON.stringify(requestPayload, null, 2);
  const responseText = JSON.stringify(responsePayload, null, 2);
  traceBox.textContent =
    `POST /moderate\n\nRequest:\n${requestText}\n\nStatus: ${statusCode}\nResponse:\n${responseText}`;
}

async function checkHealth() {
  try {
    const response = await fetch("/health");
    setApiStatus(response.ok);
  } catch (error) {
    setApiStatus(false);
  }
}

analyzeBtn.addEventListener("click", async () => {
  clearError();

  const text = commentInput.value.trim();
  if (!text) {
    showError("Enter a comment before clicking Analyze.");
    return;
  }

  const payload = { text };
  setBusy(true);

  try {
    const response = await fetch("/moderate", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });

    const data = await response.json().catch(() => ({}));
    updateTrace(payload, data, response.status);

    if (!response.ok) {
      showError(data.detail || `Request failed with status ${response.status}.`);
      return;
    }

    renderResult(data);
  } catch (error) {
    showError("Network error while calling /moderate.");
  } finally {
    setBusy(false);
  }
});

clearBtn.addEventListener("click", () => {
  commentInput.value = "";
  resultCard.classList.add("hidden");
  clearError();
  traceBox.textContent = "No requests yet.";
  commentInput.focus();
});

checkHealth();
