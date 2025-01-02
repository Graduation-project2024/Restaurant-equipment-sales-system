function validatePassword(password) {
    // Initialize validation object
    let validation = {
        length: password.length >= 8,
        uppercase: /[A-Z]/.test(password),
        number: /[0-9]/.test(password),
        special: /[!@#$%^&*()]/.test(password)
    };

    // Update validation status
    updateValidationStatus('length', validation.length);
    updateValidationStatus('uppercase', validation.uppercase);
    updateValidationStatus('number', validation.number);
    updateValidationStatus('special', validation.special);

    return Object.values(validation).every(Boolean);
}

function updateValidationStatus(requirement, isValid) {
    const element = document.getElementById(`${requirement}-requirement`);
    if (element) {
        element.classList.toggle('valid', isValid);
        element.classList.toggle('invalid', !isValid);
    }
}

function setupPasswordValidation(passwordInput, confirmInput, requirementsList) {
    if (!passwordInput || !requirementsList) return;

    // Create requirements list if it doesn't exist
    if (requirementsList.children.length === 0) {
        const requirements = [
            { id: 'length', text: '8 أحرف على الأقل' },
            { id: 'uppercase', text: 'حرف كبير واحد على الأقل' },
            { id: 'number', text: 'رقم واحد على الأقل' },
            { id: 'special', text: 'رمز خاص واحد على الأقل (!@#$%^&*())' }
        ];

        requirements.forEach(req => {
            const li = document.createElement('li');
            li.id = `${req.id}-requirement`;
            li.textContent = req.text;
            li.classList.add('invalid');
            requirementsList.appendChild(li);
        });
    }

    // Add event listeners
    passwordInput.addEventListener('input', function() {
        validatePassword(this.value);
        if (confirmInput && confirmInput.value) {
            updatePasswordMatch(this.value, confirmInput.value);
        }
    });

    if (confirmInput) {
        confirmInput.addEventListener('input', function() {
            updatePasswordMatch(passwordInput.value, this.value);
        });
    }
}

function updatePasswordMatch(password, confirmPassword) {
    const matchRequirement = document.getElementById('match-requirement');
    if (matchRequirement) {
        const isMatch = password === confirmPassword;
        matchRequirement.classList.toggle('valid', isMatch);
        matchRequirement.classList.toggle('invalid', !isMatch);
    }
}

// Initialize validation on page load
document.addEventListener('DOMContentLoaded', function() {
    const passwordInput = document.querySelector('input[name="new_password"]');
    const confirmInput = document.querySelector('input[name="confirm_password"]');
    const requirementsList = document.querySelector('.password-requirements ul');
    
    if (passwordInput && requirementsList) {
        setupPasswordValidation(passwordInput, confirmInput, requirementsList);
    }
});
