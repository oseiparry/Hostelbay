// ============================================
// HostelLink - Main JavaScript
// ============================================

// Initialize on page load
document.addEventListener('DOMContentLoaded', function() {
    checkLoginStatus();
    initializeSmoothScroll();
});

// ============================================
// Authentication Functions
// ============================================

// Check if user is logged in
function checkLoginStatus() {
    const user = JSON.parse(localStorage.getItem('user') || 'null');
    
    if (user) {
        // Hide login/signup links
        document.querySelectorAll('.logged-out').forEach(el => {
            el.classList.add('d-none');
        });
        
        // Show logged-in user menu
        document.querySelectorAll('.logged-in').forEach(el => {
            el.classList.remove('d-none');
        });
        
        // Update user name in navbar
        const userNameEl = document.getElementById('userName');
        if (userNameEl) {
            userNameEl.textContent = user.name;
        }
        
        // Update profile page if on profile page
        updateProfilePage(user);
    }
}

// Handle Login Form Submission
function handleLogin(event) {
    event.preventDefault();
    
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    
    // Demo authentication (replace with actual backend call)
    let user = null;
    
    if (email === 'student@demo.com' && password === 'student123') {
        user = {
            id: 1,
            name: 'Sarah Johnson',
            email: email,
            role: 'student'
        };
    } else if (email === 'manager@demo.com' && password === 'manager123') {
        user = {
            id: 2,
            name: 'John Smith',
            email: email,
            role: 'manager'
        };
    } else {
        alert('Invalid credentials. Use demo credentials:\nStudent: student@demo.com / student123\nManager: manager@demo.com / manager123');
        return;
    }
    
    // Store user in localStorage
    localStorage.setItem('user', JSON.stringify(user));
    
    // Redirect based on role
    if (user.role === 'manager') {
        window.location.href = '/dashboard';
    } else {
        window.location.href = '/';
    }
}

// Handle Signup Form Submission
function handleSignup(event) {
    event.preventDefault();
    
    const fullName = document.getElementById('fullName').value;
    const email = document.getElementById('signupEmail').value;
    const password = document.getElementById('signupPassword').value;
    const confirmPassword = document.getElementById('confirmPassword').value;
    const role = document.querySelector('input[name="userRole"]:checked').value;
    
    // Validate passwords match
    if (password !== confirmPassword) {
        alert('Passwords do not match!');
        return;
    }
    
    // Validate password length
    if (password.length < 8) {
        alert('Password must be at least 8 characters long!');
        return;
    }
    
    // Create user object
    const user = {
        id: Date.now(),
        name: fullName,
        email: email,
        role: role
    };
    
    // Store user in localStorage
    localStorage.setItem('user', JSON.stringify(user));
    
    // Show success message and redirect
    alert('Account created successfully!');
    
    if (role === 'manager') {
        window.location.href = '/dashboard';
    } else {
        window.location.href = '/';
    }
}

// Logout Function
function logout() {
    if (confirm('Are you sure you want to logout?')) {
        localStorage.removeItem('user');
        window.location.href = '/';
    }
}

// Toggle Password Visibility
function togglePassword(inputId) {
    const input = document.getElementById(inputId);
    const icon = document.getElementById(inputId + '-icon');
    
    if (input.type === 'password') {
        input.type = 'text';
        icon.classList.remove('bi-eye');
        icon.classList.add('bi-eye-slash');
    } else {
        input.type = 'password';
        icon.classList.remove('bi-eye-slash');
        icon.classList.add('bi-eye');
    }
}

// ============================================
// Homepage Functions
// ============================================

// Search Hostels
function searchHostels() {
    const searchTerm = document.getElementById('searchLocation').value.toLowerCase();
    const cards = document.querySelectorAll('.hostel-card');
    let found = false;
    
    cards.forEach(card => {
        const location = card.querySelector('.text-muted').textContent.toLowerCase();
        const title = card.querySelector('.card-title').textContent.toLowerCase();
        
        if (location.includes(searchTerm) || title.includes(searchTerm)) {
            card.style.display = 'block';
            found = true;
        } else {
            card.style.display = 'none';
        }
    });
    
    // Show/hide no results message
    const noResults = document.getElementById('noResults');
    if (noResults) {
        noResults.classList.toggle('d-none', found);
    }
}

// Filter Hostels
function filterHostels() {
    const priceFilter = document.getElementById('priceFilter').value;
    const locationFilter = document.getElementById('locationFilter').value;
    const roomFilter = document.getElementById('roomFilter').value;
    
    const cards = document.querySelectorAll('.hostel-card');
    let found = false;
    
    cards.forEach(card => {
        let show = true;
        
        // Price filter
        if (priceFilter) {
            const price = parseInt(card.dataset.price);
            if (priceFilter === '0-200' && price > 200) show = false;
            if (priceFilter === '200-400' && (price < 200 || price > 400)) show = false;
            if (priceFilter === '400-600' && (price < 400 || price > 600)) show = false;
            if (priceFilter === '600+' && price < 600) show = false;
        }
        
        // Location filter
        if (locationFilter && card.dataset.location !== locationFilter) {
            show = false;
        }
        
        // Room type filter
        if (roomFilter && card.dataset.room !== roomFilter) {
            show = false;
        }
        
        card.style.display = show ? 'block' : 'none';
        if (show) found = true;
    });
    
    // Show/hide no results message
    const noResults = document.getElementById('noResults');
    if (noResults) {
        noResults.classList.toggle('d-none', found);
    }
}

// Clear All Filters
function clearFilters() {
    document.getElementById('priceFilter').value = '';
    document.getElementById('locationFilter').value = '';
    document.getElementById('roomFilter').value = '';
    document.getElementById('searchLocation').value = '';
    
    document.querySelectorAll('.hostel-card').forEach(card => {
        card.style.display = 'block';
    });
    
    const noResults = document.getElementById('noResults');
    if (noResults) {
        noResults.classList.add('d-none');
    }
}

// ============================================
// Hostel Detail Functions
// ============================================

// Handle Contact Manager Form
function handleContactManager(event) {
    event.preventDefault();
    
    // Show success modal
    const modal = new bootstrap.Modal(document.getElementById('contactModal'));
    modal.show();
    
    // Reset form
    document.getElementById('contactForm').reset();
}

// Call Manager
function callManager() {
    alert('Calling hostel manager at +1 (555) 123-4567...\n\nThis is a demo. In production, this would initiate a phone call.');
}

// ============================================
// Dashboard Functions
// ============================================

// Toggle Sidebar (Mobile)
function toggleSidebar() {
    const sidebar = document.getElementById('sidebar');
    sidebar.classList.toggle('show');
}

// Confirm Delete Hostel
function confirmDelete(hostelName) {
    const modal = new bootstrap.Modal(document.getElementById('deleteModal'));
    document.getElementById('deleteHostelName').textContent = hostelName;
    modal.show();
}

// Delete Hostel
function deleteHostel() {
    // In production, this would make an API call to delete the hostel
    alert('Hostel deleted successfully!');
    
    // Close modal
    const modal = bootstrap.Modal.getInstance(document.getElementById('deleteModal'));
    modal.hide();
    
    // Reload page (in production, would update UI dynamically)
    setTimeout(() => {
        location.reload();
    }, 500);
}

// Handle Add Hostel Form
function handleAddHostel(event) {
    event.preventDefault();
    
    // Get form data
    const formData = {
        name: document.getElementById('hostelName').value,
        price: document.getElementById('hostelPrice').value,
        address: document.getElementById('address').value,
        city: document.getElementById('city').value,
        state: document.getElementById('state').value,
        zipCode: document.getElementById('zipCode').value,
        description: document.getElementById('description').value
    };
    
    // In production, this would make an API call to save the hostel
    console.log('Hostel Data:', formData);
    
    alert('Hostel submitted for review! Our team will approve it within 24-48 hours.');
    window.location.href = '/dashboard';
}

// Handle Edit Hostel Form
function handleEditHostel(event) {
    event.preventDefault();
    
    // In production, this would make an API call to update the hostel
    alert('Hostel updated successfully!');
    window.location.href = '/dashboard';
}

// Show Admin Section
function showSection(sectionName) {
    // Hide all sections
    document.querySelectorAll('.content-section').forEach(section => {
        section.classList.add('d-none');
    });
    
    // Show selected section
    const section = document.getElementById(sectionName + 'Section');
    if (section) {
        section.classList.remove('d-none');
    }
    
    // Update active link
    document.querySelectorAll('.sidebar-link').forEach(link => {
        link.classList.remove('active');
    });
    event.target.classList.add('active');
}

// ============================================
// Contact Page Functions
// ============================================

// Handle Contact Form
function handleContactForm(event) {
    event.preventDefault();
    
    const message = document.getElementById('message').value;
    
    if (message.length < 20) {
        alert('Message must be at least 20 characters long!');
        return;
    }
    
    // Show success modal
    const modal = new bootstrap.Modal(document.getElementById('contactSuccessModal'));
    modal.show();
    
    // Reset form
    document.getElementById('contactFormPage').reset();
}

// ============================================
// Profile Page Functions
// ============================================

// Update Profile Page with User Data
function updateProfilePage(user) {
    const profileName = document.getElementById('profileName');
    const profileEmail = document.getElementById('profileEmail');
    const profileRole = document.getElementById('profileRole');
    const managerName = document.getElementById('managerName');
    
    if (profileName) profileName.textContent = user.name;
    if (profileEmail) profileEmail.textContent = user.email;
    if (profileRole) {
        profileRole.textContent = user.role === 'manager' ? 'Hostel Manager' : 'Student';
    }
    if (managerName) managerName.textContent = user.name.split(' ')[0];
}

// Toggle Edit Mode
function toggleEdit(formId) {
    const form = document.getElementById(formId + 'Form');
    const inputs = form.querySelectorAll('input, textarea');
    const buttons = document.getElementById(formId + 'Buttons');
    
    inputs.forEach(input => {
        input.disabled = !input.disabled;
    });
    
    buttons.classList.toggle('d-none');
}

// Cancel Edit
function cancelEdit(formId) {
    const form = document.getElementById(formId + 'Form');
    const inputs = form.querySelectorAll('input, textarea');
    const buttons = document.getElementById(formId + 'Buttons');
    
    inputs.forEach(input => {
        input.disabled = true;
    });
    
    buttons.classList.add('d-none');
    form.reset();
}

// Handle Update Profile
function handleUpdateProfile(event) {
    event.preventDefault();
    
    // Show success modal
    const modal = new bootstrap.Modal(document.getElementById('successModal'));
    modal.show();
    
    // Disable inputs
    toggleEdit('personalInfo');
}

// Handle Change Password
function handleChangePassword(event) {
    event.preventDefault();
    
    const newPassword = document.getElementById('newPassword').value;
    const confirmPassword = document.getElementById('confirmNewPassword').value;
    
    if (newPassword !== confirmPassword) {
        alert('Passwords do not match!');
        return;
    }
    
    if (newPassword.length < 8) {
        alert('Password must be at least 8 characters!');
        return;
    }
    
    alert('Password changed successfully!');
    document.getElementById('passwordForm').reset();
}

// Save Notification Settings
function saveNotificationSettings() {
    const settings = {
        email: document.getElementById('emailNotifications').checked,
        sms: document.getElementById('smsNotifications').checked,
        marketing: document.getElementById('marketingEmails').checked
    };
    
    // In production, save to backend
    console.log('Notification Settings:', settings);
    alert('Notification preferences saved!');
}

// Confirm Delete Account
function confirmDeleteAccount() {
    const modal = new bootstrap.Modal(document.getElementById('deleteAccountModal'));
    modal.show();
}

// Delete Account
function deleteAccount() {
    const confirmation = document.getElementById('deleteConfirmation').value;
    
    if (confirmation !== 'DELETE') {
        alert('Please type DELETE to confirm');
        return;
    }
    
    // In production, call API to delete account
    alert('Account deleted successfully. We\'re sorry to see you go!');
    localStorage.removeItem('user');
    window.location.href = '/';
}

// ============================================
// Utility Functions
// ============================================

// Smooth Scroll
function initializeSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const href = this.getAttribute('href');
            if (href !== '#' && href !== '#!') {
                e.preventDefault();
                const target = document.querySelector(href);
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            }
        });
    });
}

// Format Currency
function formatCurrency(amount) {
    return '$' + amount.toLocaleString();
}

// Validate Email
function validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
}

// Validate Phone
function validatePhone(phone) {
    const re = /^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$/;
    return re.test(phone);
}

// Show Toast Notification
function showToast(message, type = 'success') {
    // Create toast element
    const toastHTML = `
        <div class="toast align-items-center text-white bg-${type} border-0" role="alert">
            <div class="d-flex">
                <div class="toast-body">${message}</div>
                <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast"></button>
            </div>
        </div>
    `;
    
    // Add to page and show
    const container = document.createElement('div');
    container.className = 'toast-container position-fixed bottom-0 end-0 p-3';
    container.innerHTML = toastHTML;
    document.body.appendChild(container);
    
    const toast = new bootstrap.Toast(container.querySelector('.toast'));
    toast.show();
    
    // Remove after hidden
    container.querySelector('.toast').addEventListener('hidden.bs.toast', () => {
        container.remove();
    });
}

// Debounce Function
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// ============================================
// Image Upload Preview
// ============================================
const hostelImagesInput = document.getElementById('hostelImages');
if (hostelImagesInput) {
    hostelImagesInput.addEventListener('change', function(e) {
        const preview = document.getElementById('imagePreview');
        if (preview) {
            preview.innerHTML = '';
            
            Array.from(e.target.files).forEach((file, index) => {
                if (file.type.startsWith('image/')) {
                    const reader = new FileReader();
                    reader.onload = function(e) {
                        const img = document.createElement('img');
                        img.src = e.target.result;
                        img.className = 'img-thumbnail';
                        img.style.width = '100px';
                        img.style.height = '100px';
                        img.style.objectFit = 'cover';
                        preview.appendChild(img);
                    };
                    reader.readAsDataURL(file);
                }
            });
        }
    });
}

// ============================================
// Console Welcome Message
// ============================================
console.log('%cHostelLink', 'font-size: 24px; font-weight: bold; color: #0A74DA;');
console.log('%cWelcome to HostelLink! Find your perfect student accommodation.', 'font-size: 14px; color: #6B7280;');