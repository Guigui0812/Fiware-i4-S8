// Script for adding more keyword boxes
function addKeyWordBox() {
    var form = document.getElementById("keyword");
    var input = document.createElement("input");
    input.setAttribute("type", "text");
    input.setAttribute("name", "keyword");
    input.setAttribute("placeholder", "Enter a keyword");
    input.classList.add('appearance-none', 'block', 'w-full', 'bg-gray-800', 'text-white', 'border', 'border-gray-700', 'rounded', 'py-3', 'px-4', 'mb-3', 'leading-tight', 'focus:outline-none', 'focus:bg-gray-700');
    input.setAttribute("required", "required");
    form.appendChild(input);
}

// Script for adding more Job type boxes
function addJobTypeBox() {
    var form = document.getElementById("jobtype");
    var input = document.createElement("select");
    input.setAttribute("name", "job");
    input.classList.add('appearance-none', 'block', 'w-full', 'bg-gray-800', 'text-white', 'border', 'border-gray-700', 'rounded', 'py-3', 'px-4', 'mb-3', 'leading-tight', 'focus:outline-none', 'focus:bg-gray-700');
    input.setAttribute("required", "required");
    input.innerHTML =  '<option value="">-- Choisissez un job --</option>'
    + '<option value="developpeur">Développeur</option>'
    + '<option value="devops">DevOps</option>'
    + '<option value="ingenieur-reseau">Ingénieur Réseau</option>'
    + '<option value="administrateur-systeme">Administrateur Système</option>'
    + '<option value="data-engineer">Data Engineer</option>'
    + '<option value="software-engineer">Software Engineer</option>'
    + '</select>';
    form.appendChild(input);
}

// Login AJAX request (check si je dois faire une promise)
function login(event) {
    event.preventDefault();
    fetch('/login', {
        method: 'POST',
        body: JSON.stringify({
            username: document.getElementById('username').value,
            password: document.getElementById('password').value
        }),
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            window.location.href = '/jobs';
        } else {
            document.getElementById('login-error').innerHTML = data.message;
        }
    })
    .catch(error => console.error(error));
}

// Generate letter AJAX request
function generateMotivationLetter(button, event){
    event.preventDefault();

    const parentDiv = button.closest('.bg-gray-800'); // sélectionne la div parente
    const descriptionElement = parentDiv.querySelector('p[name="description"]'); // sélectionne le <p> ayant name="description"
    const descriptionContent = descriptionElement.textContent; // récupère le contenu textuel du <p>
    
    console.log(descriptionContent);

    fetch('/generate', {
        method: 'POST',
        body: JSON.stringify({
            description: descriptionContent
        }),
        headers: {
            'Content-Type': 'application/json' 
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            console.log(data.message);
        } else {
            console.log(data.message);
        }
    })
}