module.exports = {
  content: [
    './templates/**/*.html',
    './**/templates/**/*.html',
    './**/*.py',
  ],
  theme: {
    extend: {
      colors: {
        primary: '#0057B8', // Ukrainian Flag Blue
        secondary: '#FFD700', // Ukrainian Flag Yellow
        dark: '#212529', // Dark Gray Text
        privatbank: '#74B119', // PrivatBank Green
      },
      fontFamily: {
        sans: ['Inter', 'sans-serif'],
        heading: ['Montserrat', 'sans-serif'],
      },
      maxWidth: {
        '8xl': '1240px',
      },
    },
  },
  plugins: [],
}

