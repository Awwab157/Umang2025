# PowerShell script to update all sports pages to remove dark mode toggle and set light theme

$sportsFiles = @(
    "tennis.html",
    "tabletennis.html", 
    "throwball.html",
    "volleyball.html",
    "chess.html",
    "badminton.html",
    "kabaddi.html"
)

$basePath = "c:\Users\HONOR\Desktop\SEM-3\Umang2025\"

foreach ($file in $sportsFiles) {
    $filePath = Join-Path $basePath $file
    Write-Host "Processing $file..."
    
    # Read file content
    $content = Get-Content $filePath -Raw
    
    # Comment out navigation dark mode classes
    $content = $content -replace 'class="text-gray-700 dark:text-white hover:text-primary transition"', 'class="text-gray-700 /* dark:text-white */ hover:text-primary transition"'
    
    # Comment out mobile nav dark mode classes
    $content = $content -replace 'class="fixed top-0 left-0 w-full h-screen bg-white dark:bg-black z-50', 'class="fixed top-0 left-0 w-full h-screen bg-white /* dark:bg-black */ z-50'
    $content = $content -replace 'class="absolute top-5 right-8 text-gray-700 dark:text-gray-200"', 'class="absolute top-5 right-8 text-gray-700 /* dark:text-gray-200 */"'
    
    # Remove mobile dark toggle button completely
    $content = $content -replace '<button id="mobile-dark-toggle"[^>]*>[\s\S]*?</button>', '<!-- <button id="mobile-dark-toggle" class="mt-8 px-4 py-2 rounded-xl bg-primary text-white font-semibold shadow hover:bg-[#003b5c] transition">
        <span id="mobile-toggle-text">Toggle Dark Mode</span>
      </button> -->'
    
    # Comment out dark mode CSS
    $content = $content -replace '\.dark \.glass-effect \{[\s\S]*?\}', '/* .dark .glass-effect {
        background: rgba(0, 0, 0, 0.3);
        border: 1px solid rgba(255, 255, 255, 0.1);
    } */'
    
    $content = $content -replace '\.dark \.hover-scale:hover \{[\s\S]*?\}', '/* .dark .hover-scale:hover {
        box-shadow: 0 20px 40px rgba(0, 119, 182, 0.5);
    } */'
    
    # Comment out dark mode JavaScript
    $content = $content -replace '// Dark mode toggle functions[\s\S]*?// Set default to light mode and load saved preference[\s\S]*?\}', '// Dark mode toggle functions
    /* function toggleDarkMode() {
      document.documentElement.classList.toggle("dark");
      const isDark = document.documentElement.classList.contains("dark");
      
      // Update button text
      const desktopText = document.getElementById("desktop-toggle-text");
      const mobileText = document.getElementById("mobile-toggle-text");
      desktopText.textContent = isDark ? '"'"'Toggle Light'"'"' : '"'"'Toggle Dark'"'"';
      mobileText.textContent = isDark ? '"'"'Toggle Light Mode'"'"' : '"'"'Toggle Dark Mode'"'"';
      
      // Close mobile menu if open
      document.getElementById("mobile-nav").style.display = "none";
      document.body.style.overflow = "";
      
      // Save preference
      localStorage.setItem('"'"'darkMode'"'"', isDark);
    }
    
    // Desktop dark mode toggle
    document.getElementById("desktop-dark-toggle").onclick = toggleDarkMode;
    
    // Mobile dark mode toggle
    document.getElementById("mobile-dark-toggle").onclick = toggleDarkMode;
    
    // Set default to light mode and load saved preference
    document.documentElement.classList.remove('"'"'dark'"'"');
    if (localStorage.getItem('"'"'darkMode'"'"') === '"'"'true'"'"') {
      document.documentElement.classList.add('"'"'dark'"'"');
      const desktopText = document.getElementById("desktop-toggle-text");
      const mobileText = document.getElementById("mobile-toggle-text");
      if (desktopText) desktopText.textContent = '"'"'Toggle Light'"'"';
      if (mobileText) mobileText.textContent = '"'"'Toggle Light Mode'"'"';
    } */'
    
    # Comment out dark mode classes in content sections
    $content = $content -replace 'dark:bg-background-dark', '/* dark:bg-background-dark */'
    $content = $content -replace 'dark:text-white', '/* dark:text-white */'
    $content = $content -replace 'dark:text-gray-200', '/* dark:text-gray-200 */'
    $content = $content -replace 'dark:text-gray-300', '/* dark:text-gray-300 */'
    $content = $content -replace 'dark:text-gray-400', '/* dark:text-gray-400 */'
    $content = $content -replace 'dark:text-gray-500', '/* dark:text-gray-500 */'
    $content = $content -replace 'dark:bg-black', '/* dark:bg-black */'
    
    # Write back to file
    Set-Content -Path $filePath -Value $content -Encoding UTF8
    
    Write-Host "Completed $file"
}

Write-Host "All sports pages updated successfully!"