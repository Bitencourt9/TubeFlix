# 🎬 TubeFlix - Seu Hub de Vídeos Personalizado!

<p align="center">
  <img src="https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellowgreen" alt="Status do Projeto">
  <img src="https://img.shields.io/badge/Tecnologias-HTML%20%7C%20CSS%20%7C%20Django-blue" alt="Tecnologias">
  <img src="https://img.shields.io/badge/Licen%C3%A7a-MIT-green" alt="Licença">
</p>

---

## 🌟 Sobre o Projeto

O **TubeFlix** é uma plataforma de vídeos, inspirada em grandes serviços como Netflix e YouTube. Este projeto permite que usuários façam upload de seus próprios vídeos, assistam a vídeos de outros usuários, curtam e deixem comentários. É uma aplicação robusta desenvolvida com **Django** (Python) no backend e **HTML/CSS** para uma interface de usuário responsiva e intuitiva, com um toque visual minimalista e moderno.

### ✨ Funcionalidades Principais:

* **Upload de Vídeos:** Usuários registrados podem facilmente enviar seus próprios vídeos para a plataforma, adicionando título, descrição e thumbnail.
* **Visualização de Vídeos:** Assista a vídeos com um player HTML5 responsivo.
* **Curtir/Descurtir Vídeos:** Interaja com o conteúdo marcando seus vídeos favoritos.
* **Comentários:** Deixe comentários nos vídeos e veja a opinião de outros usuários.
* **Página de Perfil:** Gerencie seus próprios vídeos e comentários em uma área dedicada.
* **Interface Intuitiva:** Design limpo e inspirado em plataformas de streaming populares.

---

## 🛠️ Tecnologias Utilizadas

* **Backend:**
    * **Python:** Linguagem de programação principal.
    * **Django:** Framework web de alto nível para o desenvolvimento rápido e seguro.
    * **Pillow:** Biblioteca para manipulação de imagens (thumbnails).
* **Frontend:**
    * **HTML5:** Estrutura da página.
    * **CSS3:** Estilização responsiva e moderna, com foco em cores escuras e tipografia limpa (Roboto).
* **Banco de Dados:**
    * **SQLite3:** Banco de dados padrão do Django (para desenvolvimento).
* **Controle de Versão:**
    * **Git:** Para o controle de versão do código.
    * **GitHub:** Hospedagem do repositório de código.

---

## 🚀 Como Executar o Projeto Localmente

Siga estes passos para ter o TubeFlix rodando na sua máquina:

### Pré-requisitos

Certifique-se de ter instalado:

* **Python 3.x** ([python.org](https://www.python.org/downloads/))
* **Git** ([git-scm.com](https://git-scm.com/))

### Passos:

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/Bitencourt9/TubeFlix.git](https://github.com/Bitencourt9/TubeFlix.git)
    cd TubeFlix
    ```

2.  **Crie e ative um ambiente virtual:**
    É uma boa prática para isolar as dependências do projeto.
    ```bash
    python -m venv venv
    ```
    * **No Windows (PowerShell):**
        ```bash
        .\venv\Scripts\activate
        ```
    * **No macOS/Linux/Git Bash:**
        ```bash
        source venv/bin/activate
        ```

3.  **Instale as dependências:**
    Com seu ambiente virtual ativo, instale todas as bibliotecas necessárias listadas no `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute as migrações do banco de dados:**
    ```bash
    python manage.py migrate
    ```

5.  **Crie um superusuário (opcional, para acesso ao painel de administração):**
    ```bash
    python manage.py createsuperuser
    ```
    Siga as instruções no terminal para criar seu usuário e senha.

6.  **Inicie o servidor de desenvolvimento:**
    ```bash
    python manage.py runserver
    ```

7.  **Acesse o projeto:**
    Abra seu navegador e vá para `http://127.0.0.1:8000/`

---

## 🤝 Contribuição

Contribuições são sempre bem-vindas! Se você tiver ideias, sugestões ou encontrar bugs, sinta-se à vontade para:

1.  Fazer um **fork** do repositório.
2.  Criar uma **branch** para sua funcionalidade (`git checkout -b feature/minha-nova-feature`).
3.  Fazer seus **commits** (`git commit -m 'feat: adiciona nova funcionalidade X'`).
4.  Fazer **push** para a branch (`git push origin feature/minha-nova-feature`).
5.  Abrir um **Pull Request**.

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 📞 Contato

Lucas Bitencourt - lucasbitencourt582@gmail.com

---