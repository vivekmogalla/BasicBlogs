document.addEventListener('DOMContentLoaded', () => {
  // JavaScript code to handle the "Read more" functionality
  const buttons = document.querySelectorAll('.read-more-btn');
  debugger;
  buttons.forEach((button) => {
    button.addEventListener('click', () => {
      const blogInfo = button.parentElement;
      const blogContent = blogInfo.querySelector('.blog-content');
      const fullContent = blogInfo.querySelector('.full-content');

      if (blogContent.style.display === 'none') {
        blogContent.style.display = 'block';
        fullContent.style.display = 'none';
        button.textContent = 'Read more';
      } else {
        blogContent.style.display = 'none';
        fullContent.style.display = 'block';
        button.textContent = 'Read less';
      }
    });
  });
});
