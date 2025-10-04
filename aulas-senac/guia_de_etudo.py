# prototipo_guia_estudos.py
from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
import time
import threading

# Função de alarme simples
def lembrete_estudo(horario, mensagem="Hora de estudar!"):
    def verificar():
        while True:
            agora = time.strftime("%H:%M")
            if agora == horario:
                print(f"⏰ {mensagem}")
                break
            time.sleep(30)
    t = threading.Thread(target=verificar)
    t.start()

# Estrutura principal
class GuiaEstudos(TabbedPanel):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.do_default_tab = False

        # Aba de Teoria
        teoria = BoxLayout(orientation="vertical")
        teoria.add_widget(Label(text="Conteúdo Teórico\n(JS e Python)", font_size=18))
        teoria.add_widget(Label(text="- Conceitos básicos\n- Estruturas de dados\n- Sintaxe"))
        self.add_widget(teoria)

        # Aba de Exercícios
        exercicios = BoxLayout(orientation="vertical")
        exercicios.add_widget(Label(text="Exercícios Práticos", font_size=18))
        exercicios.add_widget(Label(text="- Listas de desafios\n- Algoritmos\n- Mini projetos"))
        self.add_widget(exercicios)

        # Aba de Revisão/Tarefas
        revisao = BoxLayout(orientation="vertical")
        self.input_tarefa = TextInput(hint_text="Adicionar revisão ou tarefa...")
        revisao.add_widget(self.input_tarefa)
        btn_add = Button(text="Salvar Tarefa")
        btn_add.bind(on_release=self.adicionar_tarefa)
        revisao.add_widget(btn_add)
        self.lista_tarefas = Label(text="Nenhuma tarefa ainda.")
        revisao.add_widget(self.lista_tarefas)
        self.add_widget(revisao)

        # Aba de Lembretes
        lembretes = BoxLayout(orientation="vertical")
        self.input_hora = TextInput(hint_text="Digite hora (HH:MM)")
        lembretes.add_widget(self.input_hora)
        btn_lembrete = Button(text="Definir lembrete")
        btn_lembrete.bind(on_release=self.definir_lembrete)
        lembretes.add_widget(btn_lembrete)
        self.add_widget(lembretes)

    def adicionar_tarefa(self, instance):
        tarefa = self.input_tarefa.text
        if tarefa.strip():
            self.lista_tarefas.text += f"\n- {tarefa}"
            self.input_tarefa.text = ""

    def definir_lembrete(self, instance):
        hora = self.input_hora.text
        if hora:
            lembrete_estudo(hora)
            popup = Popup(title="Lembrete Definido",
                          content=Label(text=f"Lembrete para {hora}"),
                          size_hint=(0.6, 0.4))
            popup.open()


class GuiaEstudosApp(App):
    def build(self):
        return GuiaEstudos()


if __name__ == "__main__":
    GuiaEstudosApp().run()
