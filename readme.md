def login_view(request):
    if request.method == 'POST':
        # Retrieve the form data
        intranetID = request.POST.get('intranetID')
        password = request.POST.get('password')

        # Check if both fields are filled
        if intranetID and password:
            # Store the values in the session
            request.session['intranetID'] = intranetID
            request.session['password'] = password

            user = False

            if user == True:
                return redirect('source_info_page')
            else:
                return render(request, 'auth_app/login.html', {'invalid_credentials': True})

            # Redirect to the source info page
            return redirect('source_info_page')
            
        else:
            # Return the form with an error if fields are missing
            return render(request, 'auth_app/login.html', {'error': 'Please fill in both fields'})
        

<script>
    // Trigger an alert if credentials are invalid
    "{% if invalid_credentials %}"
    alert("Invalid credentials. Please try again.");
    "{% endif %}"
</script>