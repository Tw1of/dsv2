const modal = document.getElementById('create_server');
const modalBox = document.getElementById('modalBox');
const closeModalBtn = document.getElementById('close-modal-btn');
const chooseTemplateBtn = document.getElementById('choose-template-btn');
const backBtn = document.getElementById('back-btn');

let isModalOpen = false;

// Этапы
const step1 = document.querySelector('.step1');
const step2 = document.querySelector('.step2');

// Открытие модального окна на первом этапе
document.getElementById('show-modal-btn').addEventListener('click', (e) => {
    modal.classList.add('active');
    step1.classList.add('active');
    step2.classList.remove('active');
    isModalOpen = true;
    e.stopPropagation(); // предотвращает закрытие модального окна
});

// Переход ко второму этапу
chooseTemplateBtn.addEventListener('click', (e) => {
    step1.classList.remove('active');
    step2.classList.add('active');
    isModalOpen = true;
    e.stopPropagation(); // предотвращает закрытие при клике внутри
});

// Возврат к первому этапу
backBtn.addEventListener('click', (e) => {
    step2.classList.remove('active');
    step1.classList.add('active');
    isModalOpen = true;
    e.stopPropagation();
});

closeModalBtn.addEventListener('click', () => {
  modal.classList.remove('active');
  isModalOpen = false;
});

// Закрытие модального окна при клике вне его
document.addEventListener('click', (e) => {
    if (isModalOpen && !modalBox.contains(e.target)) {
        modal.classList.remove('active');
        isModalOpen = false;
    }
});
