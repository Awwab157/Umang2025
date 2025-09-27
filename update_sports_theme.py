import os
import re

# List of sports pages to update
sports_pages = [
    'badminton.html',
    'chess.html', 
    'football.html',
    'kabaddi.html',
    'tabletennis.html',
    'tennis.html',
    'throwball.html',
    'volleyball.html'
]

base_path = r'c:\Users\HONOR\Desktop\Umang2025'

for page in sports_pages:
    file_path = os.path.join(base_path, page)
    
    if os.path.exists(file_path):
        print(f"Updating {page}...")
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Update the head section with Tailwind and theme config
        head_pattern = r'(<head>.*?</head>)'
        new_head = '''<head>
    <meta charset="utf-8">
    <meta http-equiv="x-ua-compatible" content="ie=edge">
    <title>Umang 2025</title>
    <meta name="description" content="">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="manifest" href="site.webmanifest">
    <link rel="shortcut icon" type="image/x-icon" href="assets/img/favicon.ico">
    
    <!-- Home page theme integration -->
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap" rel="stylesheet" />
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet" />
    <script src="https://cdn.tailwindcss.com?plugins=forms,typography"></script>
    <script>
        tailwind.config = {
          darkMode: "class",
          theme: {
            extend: {
              colors: {
                primary: "#0077b6",
                "background-light": "#f0f8ff",
                "background-dark": "#023e8a",
              },
              fontFamily: {
                display: ["Poppins", "sans-serif"],
              },
              borderRadius: {
                xl: "1rem",
              },
            },
          },
        };
    </script>

	<!-- CSS here -->
	<link rel="stylesheet" href="assets/css/bootstrap.min.css">
	<link rel="stylesheet" href="assets/css/owl.carousel.min.css">
	<link rel="stylesheet" href="assets/css/slicknav.css">
    <link rel="stylesheet" href="assets/css/flaticon.css">
    <link rel="stylesheet" href="assets/css/gijgo.css">
	<link rel="stylesheet" href="assets/css/animate.min.css">
	<link rel="stylesheet" href="assets/css/magnific-popup.css">
	<link rel="stylesheet" href="assets/css/fontawesome-all.min.css">
	<link rel="stylesheet" href="assets/css/themify-icons.css">
	<link rel="stylesheet" href="assets/css/slick.css">
	<link rel="stylesheet" href="assets/css/nice-select.css">
	<link rel="stylesheet" href="assets/css/style.css">
</head>'''
        
        content = re.sub(head_pattern, new_head, content, flags=re.DOTALL)
        
        # Update body tag
        content = re.sub(r'<body[^>]*>', '<body class="bg-background-light dark:bg-background-dark font-display text-gray-800 dark:text-gray-200">', content)
        
        # Update color styles for about-low-area and related elements
        style_updates = {
            r'background-color: #14062E': 'background-color: #f0f8ff',
            r'color: #DF84E1': 'color: #0077b6',
            r'color: #FFFFFF': 'color: #374151',
            r'background-color: #422989': 'background-color: #0077b6',
            r'background-color: #6A3EBF': 'background-color: #003b5c',
            r'color: #FCA5FE': 'color: #0077b6'
        }
        
        for old_style, new_style in style_updates.items():
            content = re.sub(old_style, new_style, content)
        
        # Add dark mode styles
        dark_mode_css = '''        .dark .about-low-area {
            background-color: #0a2240;
        }
        .dark .about-caption ul {
            color: #d1d5db;
        }
        .dark .point-of-contact {
            color: #d1d5db;
        }
        .dark .about-caption .point-of-contact p {
            color: #d1d5db;
        }'''
        
        # Insert dark mode styles after existing styles
        content = re.sub(r'(\.point-of-contact[^}]*})', r'\1\n' + dark_mode_css, content)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Successfully updated {page}")
    else:
        print(f"File {page} not found")

print("All sports pages updated!")