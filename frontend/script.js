function buscar() {
    const autor = document.getElementById("autor").value;

    fetch(`http://127.0.0.1:5000/buscar?autor=${autor}`)
        .then(response => response.json())
        .then(data => {
            const lista = document.getElementById("resultados");
            lista.innerHTML = "";

            data.forEach(libro => {
                const li = document.createElement("li");
                li.textContent = libro[1] + " - " + libro[2];
                lista.appendChild(li);
            });
        });
}