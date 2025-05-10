document.addEventListener('DOMContentLoaded', () => {
    const input = document.getElementById('news-input');
    const placeholder = document.getElementById('input-placeholder');

    // Remove this entire existing event block and replace with:
    input.addEventListener('input', () => {
        if (input.value.trim() === '') {
            placeholder.style.display = 'block';
        } else {
            placeholder.style.display = 'none';
        }
    });
});