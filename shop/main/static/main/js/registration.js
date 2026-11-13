document.getElementById("registerForm").addEventListener("submit", async function(e) {

    e.preventDefault();

    const form = e.target;
    const formData = new FormData(form);

    const csrfToken = form.querySelector('[name="csrfmiddlewaretoken"]').value;

    try {

        const response = await fetch(form.action, {
            method: "POST",
            headers: {
                "X-CSRFToken": csrfToken
            },
            body: formData
        });

        const result = await response.json();

        console.log(result);

        if (response.ok) {

            document.getElementById("result").innerHTML =
                '<div class="alert alert-success">Реєстрація успішна!</div>';

            form.reset();

        } else {

            document.getElementById("result").innerHTML =
                '<div class="alert alert-danger">' + result.message + '</div>';

        }

    } catch (error) {

        console.error("Помилка:", error);

    }

});
