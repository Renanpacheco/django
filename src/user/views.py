from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import CadastroForm


def index(request):
    
    eventos_teste = [
        {
            'nome': 'Workshop de Branding',
            'horario': '15/05/2026 às 14:00',
            'local': 'Auditório Principal',
            'descricao': 'Aprenda estratégias de branding para posicionamento de mercado com foco em agências.'
        },
        {
            'nome': 'Pedalada Ecológica',
            'horario': '20/05/2026 às 09:30',
            'local': 'Laranjal',
            'descricao': 'Se junte a esse grupo e pedale conosco em um passeio ecológico pela cidade, promovendo saúde e sustentabilidade.'
        },
        {
            'nome': 'Show Simone Mendes',
            'horario': '30/04/2026 às 21:00',
            'local': 'Centro de Eventos Fenadoce',
            'descricao': 'Venha curtir um show exclusivo da talentosa Simone Mendes, com repertório variado e muita energia no palco.'
        },
    ]
    
    
    return render(request, 'user/index.html', {'eventos': eventos_teste})
def login_view(request):
    return render(request, 'user/login.html')

def cadastro(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            
            pass
    else:
        form = CadastroForm() # Aqui criamos o objeto form
    
   
    return render(request, 'user/cadastro.html', {'form': form})
