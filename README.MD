# Eventos Django

## 📌 Descrição

O **Eventos Django** é uma aplicação backend desenvolvida com Django para gerenciamento de eventos e disponibilidade de horários.

A plataforma permite que usuários:

* Criem eventos
* Definam horários disponíveis
* Participem de eventos criados por outros usuários

O projeto segue uma arquitetura organizada por camadas (Layer-Based), promovendo separação de responsabilidades, escalabilidade e facilidade de manutenção.

---

## 🧱 Arquitetura

O projeto está estruturado com base em boas práticas modernas:

* **src/** → Domínios da aplicação (ex: eventos)
* **users/** → Controle dos usuários
* **Events/** → Controle dos eventos


---

## ⚙️ Pré-requisitos

Antes de começar, você precisa ter instalado:

* Python 3.10+
* pip
* Virtualenv (opcional, mas recomendado)

---

## 🚀 Como rodar o projeto

### 1. Clonar o repositório

```bash
git clone <url-do-repositorio>
cd eventos-django
```

---

### 2. Criar e ativar ambiente virtual

```bash
python -m venv venv
```

#### Linux / Mac

```bash
source venv/bin/activate
```


---

### 3. Instalar Django

```bash
python -m pip install Django
```

---

### 4. Rodar migrations

```bash
python manage.py migrate
```

---


### 5. Iniciar o servidor

```bash
python manage.py runserver
```


---

## 🎯 Objetivo do Projeto

* Praticar arquitetura backend moderna com Django
* Implementar separação de responsabilidades (services, selectors, API)
* Servir como base para aplicações escaláveis

