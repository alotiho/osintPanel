async function callApi(endpoint, fieldName, inputId, resultId) {
    const value = document.getElementById(inputId).value.trim();
    const resultEl = document.getElementById(resultId);

    if (!value) {
        resultEl.textContent = "Введите значение";
        return;
    }

    resultEl.textContent = "Загрузка...";

    try {
        const resp = await fetch(`/api/${endpoint}`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ [fieldName]: value }),
        });
        const data = await resp.json();
        resultEl.textContent = JSON.stringify(data, null, 2);
    } catch (err) {
        resultEl.textContent = `Ошибка: ${err.message}`;
    }
}
