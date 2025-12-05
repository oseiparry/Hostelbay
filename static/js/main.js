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