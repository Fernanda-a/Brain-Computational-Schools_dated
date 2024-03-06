
#from .models import User
#from .control import checkUser


from browser import document, html, window

container = document['content']
container.html = " "


def signIn():
    div = html.DIV(id="container")
    title = html.H1("Login")
    input_name = html.INPUT(type="email", id="email", value="E-mail")
    input_password = html.INPUT(type="text", id="password", value="Password")
    input_enter = html.INPUT(type="submit", value = "Enter")
    form = html.FORM()
    form <= title + input_name + input_password + input_enter

    header = html.BUTTON("Não tem uma conta? Cadastre-se agora!")
    def signUp_go(ev):
        container.clear()
        signUp()
    def enter_bt(ev):
        #checkUser(document['email'].value, document['password'].value)
        pass
    input_enter.bind("click", enter_bt)

    header.bind("click", signUp_go)

    footer = html.P("&copy;IgorandasINC")
    div = header + form + footer
    container <= div

    
    return True


def signUp():
  div = html.DIV(id='container')

  title = html.H1('Cadastro')

  input_name = html.INPUT(type='text', id='name', placeholder='Nome')
  input_password = html.INPUT(type='text', id='password', placeholder='Senha')
  input_email = html.INPUT(type='email', id='email', placeholder='Email')
  input_cellphone = html.INPUT(type='tel', id='tel', placeholder='Celular')

  #O SELECT É PARA SER FEITO ASSIM
#   from browser import document as doc
# from browser import html, alert

# def update_select(ev):
#     # selects / deselects options in the SELECT box
#     # ev.target is the checkbox we just clicked
#     rank = choices.index(ev.target.value)
#     sel.options[rank].selected = ev.target.checked

# def show_selected(ev):
#     alert([option.value for option in sel if option.selected])

# def update_checkboxes(ev):
#     # updates checkboxes when the selection has changed
#     selected = [option.value for option in sel if option.selected]
#     for elt in doc.get(selector='input[type="checkbox"]'):
#         elt.checked = elt.value in selected

# choices = ["one","two","three","four","five"]
# sel = html.SELECT(size=5, multiple=True)
# for item in choices:
#     sel <= html.OPTION(item)
# sel.bind("change", update_checkboxes)

# for item in choices:
#     chbox = html.INPUT(Type="checkbox", value=item)
#     chbox.bind("click", update_select)
#     doc["panel"] <= item + chbox

# doc["panel"] <= sel

# b_show = html.BUTTON("show selected")
# b_show.bind("click", show_selected)
# doc["panel"] <= b_show
  
  #MAS EU FIZ ASSIM IGUAL TA AI EMBAIXO, TCHAU. TALVEZ EU CONSERTE DEPOIS

  gender = html.SELECT(name='Gender')
  female = html.OPTION(value='Mulher')
  male = html.OPTION(value='Homem')
  non_binary = html.OPTION(value='Não Binário')

  occupation_form = html.FORM(id='occupation_form')
  professional = html.INPUT(type='checkbox', placeholder='Profissional')
  student = html.INPUT(type='checkbox', placeholder='Estudante')
  pacient = html.INPUT(type='checkbox', placeholder='Paciente')

  field = html.SELECT(name='Field')
  #campo onde da para adicionar as áreas
  career = html.SELECT(name='Career')
  #campo onde da para adicoinar as profissoes

  photo = html.INPUT(type='image', value='Foto')

  terms_agreement = html.INPUT(type='checkbox', placeholder='Li e concordo com os Termos de Usuário')

  sign_up_wrapper_form = html.FORM(id='sign_up_wrapper_form')

  submit = html.INPUT(type='submit', id='submit', value='Enviar')

  gender <= female + male + non_binary
  occupation_form <= professional + student + pacient

  go_to_signIn = html.BUTTON("Já tem uma conta? Faça login!")

  sign_up_wrapper_form <= go_to_signIn + title + input_name + input_password + input_email + input_cellphone + gender + occupation_form + field + career + photo + terms_agreement + submit

  def goToSignIn(ev):
    container.clear()
    signIn()

  go_to_signIn.bind("click", goToSignIn)
  
  def send_wrapper_form(ev):
    #fazer um código para mandar para a main page
    print('')

  container <= sign_up_wrapper_form

def home():
    div = html.DIV(id="container")
    menu = html.P("menu")
    profile = html.P("menu")
    about = html.P("menu")
    models3D = html.P("menu")
    user_sugestion = html.P("menu")

    header = html.BUTTON("Não tem uma conta? Cadastre-se agora!")
    def signUp_go(ev):
        container.clear()
        signUp()
    
    header.bind("click", signUp_go)
    footer = html.P("&copy;Igorandas")
    div = header + form + footer
    container <= div

    return True

signIn()









