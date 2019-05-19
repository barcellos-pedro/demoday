let x = document.querySelector('.fecha');
let modal = document.querySelector('.login-container');
let cancelar = document.querySelector('.btnCancelar');
let entrarNav = document.querySelector('#entrarNav');

function troca(){
    modal.classList.toggle('aparecer');
}


x.onclick = troca;
cancelar.onclick = troca; 
entrarNav.onclick = troca;