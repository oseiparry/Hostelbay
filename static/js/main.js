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

document.addEventListener('DOMContentLoaded', function () {
    showSection('users');
});


function toggleSidebar() {
    document.getElementById("sidebar").classList.toggle("open");
}

function showSection(section) {
    document.querySelectorAll(".content-section").forEach(sec => {
        sec.classList.add("d-none");
    });

    document.getElementById(section + "Section").classList.remove("d-none");
}

function showSection(section) {
    // hide all sections
    document.querySelectorAll('.content-section').forEach(el => {
        el.classList.add('d-none');
    });

    // show selected section
    const target = document.getElementById(section + 'Section');
    if (target) {
        target.classList.remove('d-none');
    }

    // active sidebar link
    document.querySelectorAll('.sidebar-link').forEach(link => {
        link.classList.remove('active');
    });

    event.currentTarget.classList.add('active');
}


// ============================================
// Console Welcome Message
// ============================================
console.log('%cHostelLink', 'font-size: 24px; font-weight: bold; color: #0A74DA;');
console.log('%cWelcome to HostelLink! Find your perfect student accommodation.', 'font-size: 14px; color: #6B7280;');
