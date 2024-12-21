from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Product, Chat
import json
from django.contrib.auth import logout


def custom_logout_view(request):
    logout(request)  # Clears the session and logs out the user
    return redirect('login')  # Redirect to the login page


# -------------------- SIGNUP VIEW --------------------

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('chat')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

# -------------------- CHAT VIEW --------------------

@login_required
def chat(request):
    return render(request, 'chat.html')

# -------------------- COMPONENT HANDLING FUNCTIONS --------------------

def handle_product_details(user_message):
    """Handles product details request."""
    product = Product.objects.filter(model_name__iexact=user_message).first()
    if product:
        return (f"Product: {product.model_name}<br>"
                f"Details: {product.details}<br>"
                f"Price: ₹{product.price}<br>"
                f"Here is the Link of the product : #Link#")
    else:
        return "Model not found. Please check the model name and try again."

def handle_price(user_message):
    """Handles price request."""
    product = Product.objects.filter(model_name__iexact=user_message).first()
    if product:
        return f"The price of {product.model_name} is ₹{product.price}."
    else:
        return "Model not found. Please check the model name and try again."

def handle_product_status(user_message):
    """Handles product status request."""
    product = Product.objects.filter(model_name__iexact=user_message).first()

    return f"The Status of your product is :"
   

def handle_any_other():
    """Handles custom queries."""
    return "Your response is stored. Our executive team will get in touch with you within a few minutes."

# -------------------- CHAT API --------------------

@login_required
def chat_api(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            user_message = data.get('message').strip().lower()

            # Initialize response variable
            response = ""

            if user_message == 'start':
                response = ("What can I do for you....<br> Simply type '1','2','3','4'<br><br>1. Know product details <br> 2. Know product price<br> 3. Status of your product<br>4. Any other")
                           
                          
                            
                           
            elif user_message == '1':
                response = "Please provide the model name to know product details:<br> USE 'Model:' before model name"
                    
            elif user_message == '2':
                response = "Please provide the model name to know the price:<br> USE 'Price:' before model name"
            elif user_message == '3':
                response = "Please provide the Product ID to know the status:<br> USE 'Status:' before product Id"
            elif user_message == '4':
                response = "Please write your query:<br> USE 'Query:' before enter your query"

            # Handle specific inputs based on context
            elif user_message.startswith('model:'):
                model_name = user_message.replace('model:', '').strip()
                response = handle_product_details(model_name)
            elif user_message.startswith('price:'):
                model_name = user_message.replace('price:', '').strip()
                response = handle_price(model_name)
            elif user_message.startswith('status:'):
                model_name = user_message.replace('status:', '').strip()
                response = handle_product_status(model_name)
            elif user_message.startswith('query:'):
                response = handle_any_other()
            else:
                response = "Invalid option. Please type 'start' to begin again."

            # Save the chat message and response in the Chat model
            Chat.objects.create(user=request.user, query_type="user_message", user_input=user_message, response=response)

            # Return the response as JSON
            return JsonResponse({'response': response})
        
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON format'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=400)
