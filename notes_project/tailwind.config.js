/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: 'class', // lub 'media' według preferencji systemowych
  content: [
      './notes_app/templates/**/*.html', // Ścieżki do szablonów, które będą przetwarzane przez Tailwind CSS
  ],
  theme: {
      extend: {},
  },
  plugins: [],
}

