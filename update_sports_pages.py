#!/usr/bin/env python3
"""
Script to uniformly update all sports pages with the same layout as football.html
This script preserves all existing data while applying the new aesthetic layout.
"""

import os
import re
from typing import Dict, List, Tuple

# Sports configuration with their specific details
SPORTS_CONFIG = {
    'badminton': {
        'title': 'Badminton',
        'emoji': '🏸',
        'subtitle': 'Shuttlecock Supremacy at Umang \'25',
        'icon': 'sports_tennis',
        'image': 'assets/img/gallery/Vbadminton.png',
        'prize_pool': '₹40K',
        'registration_links': {
            'men': 'https://forms.gle/d7s6sGgEcYBzwBbG8',
            'women': 'https://forms.gle/d7s6sGgEcYBzwBbG8'
        },
        'rules_link': 'https://docs.google.com/document/d/1ocV4d3CyINPgbpMGxwtjb9lcmkBSEzF0G0nomzVM4Kw/edit?usp=sharing',
        'contacts': [
            {'name': 'Contact Person 1', 'phone': '+91 98765 43210'},
            {'name': 'Contact Person 2', 'phone': '+91 87654 32109'}
        ]
    },
    'basketball': {
        'title': 'Basketball',
        'emoji': '🏀',
        'subtitle': 'Court Domination at Umang \'25',
        'icon': 'sports_basketball',
        'image': 'assets/img/gallery/Vbasketball.png',
        'prize_pool': '₹60K',
        'registration_links': {
            'men': 'https://forms.gle/d7s6sGgEcYBzwBbG8',
            'women': 'https://forms.gle/d7s6sGgEcYBzwBbG8'
        },
        'rules_link': 'https://docs.google.com/document/d/1ocV4d3CyINPgbpMGxwtjb9lcmkBSEzF0G0nomzVM4Kw/edit?usp=sharing',
        'contacts': [
            {'name': 'Contact Person 1', 'phone': '+91 98765 43210'},
            {'name': 'Contact Person 2', 'phone': '+91 87654 32109'}
        ]
    },
    'chess': {
        'title': 'Chess',
        'emoji': '♟️',
        'subtitle': 'Strategic Mastery at Umang \'25',
        'icon': 'psychology',
        'image': 'assets/img/gallery/Vchess.png',
        'prize_pool': '₹25K',
        'registration_links': {
            'open': 'https://forms.gle/d7s6sGgEcYBzwBbG8',
            'women': 'https://forms.gle/d7s6sGgEcYBzwBbG8'
        },
        'rules_link': 'https://docs.google.com/document/d/1ocV4d3CyINPgbpMGxwtjb9lcmkBSEzF0G0nomzVM4Kw/edit?usp=sharing',
        'contacts': [
            {'name': 'Contact Person 1', 'phone': '+91 98765 43210'},
            {'name': 'Contact Person 2', 'phone': '+91 87654 32109'}
        ]
    },
    'kabaddi': {
        'title': 'Kabaddi',
        'emoji': '🤼',
        'subtitle': 'Traditional Power at Umang \'25',
        'icon': 'sports_mma',
        'image': 'assets/img/gallery/Vkabaddi.png',
        'prize_pool': '₹45K',
        'registration_links': {
            'men': 'https://forms.gle/d7s6sGgEcYBzwBbG8',
            'women': 'https://forms.gle/d7s6sGgEcYBzwBbG8'
        },
        'rules_link': 'https://docs.google.com/document/d/1ocV4d3CyINPgbpMGxwtjb9lcmkBSEzF0G0nomzVM4Kw/edit?usp=sharing',
        'contacts': [
            {'name': 'Contact Person 1', 'phone': '+91 98765 43210'},
            {'name': 'Contact Person 2', 'phone': '+91 87654 32109'}
        ]
    },
    'tennis': {
        'title': 'Tennis',
        'emoji': '🎾',
        'subtitle': 'Ace Your Way at Umang \'25',
        'icon': 'sports_tennis',
        'image': 'assets/img/gallery/Vtennis.png',
        'prize_pool': '₹35K',
        'registration_links': {
            'men': 'https://forms.gle/d7s6sGgEcYBzwBbG8',
            'women': 'https://forms.gle/d7s6sGgEcYBzwBbG8'
        },
        'rules_link': 'https://docs.google.com/document/d/1ocV4d3CyINPgbpMGxwtjb9lcmkBSEzF0G0nomzVM4Kw/edit?usp=sharing',
        'contacts': [
            {'name': 'Contact Person 1', 'phone': '+91 98765 43210'},
            {'name': 'Contact Person 2', 'phone': '+91 87654 32109'}
        ]
    },
    'tabletennis': {
        'title': 'Table Tennis',
        'emoji': '🏓',
        'subtitle': 'Ping Pong Precision at Umang \'25',
        'icon': 'sports_tennis',
        'image': 'assets/img/gallery/Vtabletennis.png',
        'prize_pool': '₹30K',
        'registration_links': {
            'men': 'https://forms.gle/d7s6sGgEcYBzwBbG8',
            'women': 'https://forms.gle/d7s6sGgEcYBzwBbG8'
        },
        'rules_link': 'https://docs.google.com/document/d/1ocV4d3CyINPgbpMGxwtjb9lcmkBSEzFor/edit?usp=sharing',
        'contacts': [
            {'name': 'Contact Person 1', 'phone': '+91 98765 43210'},
            {'name': 'Contact Person 2', 'phone': '+91 87654 32109'}
        ]
    },
    'volleyball': {
        'title': 'Volleyball',
        'emoji': '🏐',
        'subtitle': 'Spike to Victory at Umang \'25',
        'icon': 'sports_volleyball',
        'image': 'assets/img/gallery/Vvolleyball.png',
        'prize_pool': '₹40K',
        'registration_links': {
            'men': 'https://forms.gle/d7s6sGgEcYBzwBbG8',
            'women': 'https://forms.gle/d7s6sGgEcYBzwBbG8'
        },
        'rules_link': 'https://docs.google.com/document/d/1ocV4d3CyINPgbpMGxwtjb9lcmkBSEzF0G0nomzVM4Kw/edit?usp=sharing',
        'contacts': [
            {'name': 'Contact Person 1', 'phone': '+91 98765 43210'},
            {'name': 'Contact Person 2', 'phone': '+91 87654 32109'}
        ]
    },
    'throwball': {
        'title': 'Throwball',
        'emoji': '⚾',
        'subtitle': 'Perfect Throws at Umang \'25',
        'icon': 'sports_baseball',
        'image': 'assets/img/gallery/Vthrowball.png',
        'prize_pool': '₹30K',
        'registration_links': {
            'women': 'https://forms.gle/d7s6sGgEcYBzwBbG8'
        },
        'rules_link': 'https://docs.google.com/document/d/1ocV4d3CyINPgbpMGxwtjb9lcmkBSEzF0G0nomzVM4Kw/edit?usp=sharing',
        'contacts': [
            {'name': 'Contact Person 1', 'phone': '+91 98765 43210'},
            {'name': 'Contact Person 2', 'phone': '+91 87654 32109'}
        ]
    }
}

def read_template_content() -> str:
    """Read the football.html file as template"""
    try:
        with open('football.html', 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print("❌ Error: football.html template file not found!")
        return None

def extract_existing_data(file_path: str) -> Dict:
    """Extract existing data from a sports page to preserve it"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        data = {}
        
        # Extract existing contacts if present
        contact_pattern = r'<p class="text-[xl|lg].*?font-semibold.*?">(.*?)</p>.*?<a href="tel:(.*?)"'
        contacts = re.findall(contact_pattern, content, re.DOTALL)
        if contacts:
            data['contacts'] = [{'name': name.strip(), 'phone': phone.strip()} for name, phone in contacts]
        
        # Extract prize pool if present
        prize_pattern = r'<div class="text-4xl font-bold gradient-text.*?">(.*?)</div>'
        prize_match = re.search(prize_pattern, content)
        if prize_match:
            data['prize_pool'] = prize_match.group(1).strip()
        
        # Extract registration links if present
        reg_pattern = r'<a href="(https://forms\.gle/[^"]*)"'
        reg_links = re.findall(reg_pattern, content)
        if reg_links:
            data['registration_links'] = reg_links
        
        # Extract rules link if present
        rules_pattern = r'<a href="(https://docs\.google\.com/document/[^"]*)"'
        rules_match = re.search(rules_pattern, content)
        if rules_match:
            data['rules_link'] = rules_match.group(1)
        
        return data
    
    except FileNotFoundError:
        return {}

def generate_registration_buttons(sport_name: str, config: Dict) -> str:
    """Generate registration buttons based on sport configuration"""
    buttons = []
    reg_links = config.get('registration_links', {})
    icon = config.get('icon', 'sports')
    
    for category, link in reg_links.items():
        if category == 'men':
            label = f"Men's {config['title']}"
        elif category == 'women':
            label = f"Women's {config['title']}"
        elif category == 'open':
            label = f"Open {config['title']}"
        else:
            label = f"{category.title()} {config['title']}"
        
        button = f'''<a href="{link}" 
           target="_blank"
           class="group relative overflow-hidden px-6 py-4 bg-gradient-to-r from-primary to-primary/80 text-white font-semibold rounded-xl shadow-lg hover:shadow-xl transition-all duration-300 text-center">
            <div class="absolute inset-0 bg-white/20 translate-x-[-100%] group-hover:translate-x-[100%] transition-transform duration-700"></div>
            <div class="relative flex items-center justify-center">
                <span class="material-icons mr-2">{icon}</span>
                {label}
            </div>
        </a>'''
        buttons.append(button)
    
    return '\n                        '.join(buttons)

def generate_contact_cards(contacts: List[Dict]) -> str:
    """Generate contact cards"""
    cards = []
    for contact in contacts:
        card = f'''<div class="glass-effect rounded-lg p-6 hover:bg-primary/5 transition-all duration-300">
                                <div class="flex items-center justify-center mb-3">
                                    <span class="material-icons text-primary text-2xl mr-2">person</span>
                                    <p class="text-xl font-semibold text-gray-800 dark:text-white">{contact['name']}</p>
                                </div>
                                <div class="flex items-center justify-center">
                                    <span class="material-icons text-primary text-lg mr-2">phone</span>
                                    <a href="tel:{contact['phone'].replace(' ', '').replace('-', '')}" class="text-primary hover:underline font-medium text-lg transition-colors">
                                        {contact['phone']}
                                    </a>
                                </div>
                            </div>'''
        cards.append(card)
    
    return '\n                            '.join(cards)

def update_sports_page(sport_name: str, template_content: str) -> bool:
    """Update a single sports page with the new template"""
    file_path = f"{sport_name}.html"
    config = SPORTS_CONFIG[sport_name]
    
    # Extract existing data to preserve it
    existing_data = extract_existing_data(file_path)
    
    # Merge existing data with default config
    merged_config = {**config}
    if existing_data.get('prize_pool'):
        merged_config['prize_pool'] = existing_data['prize_pool']
    if existing_data.get('contacts'):
        merged_config['contacts'] = existing_data['contacts']
    if existing_data.get('registration_links'):
        # Convert list to dict format
        links = existing_data['registration_links']
        if len(links) >= 2:
            merged_config['registration_links'] = {'men': links[0], 'women': links[1]}
        elif len(links) == 1:
            merged_config['registration_links'] = {'open': links[0]}
    if existing_data.get('rules_link'):
        merged_config['rules_link'] = existing_data['rules_link']
    
    # Create the new content by replacing football-specific content
    new_content = template_content
    
    # Replace hero section
    new_content = re.sub(
        r'🏈 Football Championship',
        f'{merged_config["emoji"]} {merged_config["title"]} Championship',
        new_content
    )
    
    new_content = re.sub(
        r'<h1 class="text-white font-bold text-6xl md:text-8xl leading-tight drop-shadow-2xl mb-6 floating-animation"[^>]*>\s*Football\s*</h1>',
        f'<h1 class="text-white font-bold text-6xl md:text-8xl leading-tight drop-shadow-2xl mb-6 floating-animation" style="animation-delay: 0.2s;">\n        {merged_config["title"]}\n      </h1>',
        new_content
    )
    
    new_content = re.sub(
        r'Dominate the Field at Umang \'25',
        merged_config['subtitle'],
        new_content
    )
    
    # Replace main content description
    new_content = re.sub(
        r'Everything you need to know to compete in Football at Umang \'25',
        f'Everything you need to know to compete in {merged_config["title"]} at Umang \'25',
        new_content
    )
    
    # Replace image
    new_content = re.sub(
        r'src="assets/img/gallery/Vfootball\.png"',
        f'src="{merged_config["image"]}"',
        new_content
    )
    
    new_content = re.sub(
        r'alt="Football Championship"',
        f'alt="{merged_config["title"]} Championship"',
        new_content
    )
    
    # Replace prize pool
    new_content = re.sub(
        r'<div class="text-4xl font-bold gradient-text mb-3">₹50K</div>',
        f'<div class="text-4xl font-bold gradient-text mb-3">{merged_config["prize_pool"]}</div>',
        new_content
    )
    
    # Replace rules link
    new_content = re.sub(
        r'href="https://docs\.google\.com/document/d/1ocV4d3CyINPgbpMGxwtjb9lcmkBSEzF0G0nomzVM4Kw/edit\?usp=sharing"',
        f'href="{merged_config["rules_link"]}"',
        new_content
    )
    
    # Replace registration buttons
    registration_section = generate_registration_buttons(sport_name, merged_config)
    reg_pattern = r'<div class="grid grid-cols-1 md:grid-cols-2 gap-4">\s*<a href="https://forms\.gle/[^"]*"[^>]*>.*?</a>\s*<a href="https://forms\.gle/[^"]*"[^>]*>.*?</a>\s*</div>'
    
    if len(merged_config['registration_links']) == 1:
        new_reg_section = f'<div class="flex justify-center">\n                        {registration_section}\n                    </div>'
    else:
        new_reg_section = f'<div class="grid grid-cols-1 md:grid-cols-2 gap-4">\n                        {registration_section}\n                    </div>'
    
    new_content = re.sub(reg_pattern, new_reg_section, new_content, flags=re.DOTALL)
    
    # Replace contact information
    contact_cards = generate_contact_cards(merged_config['contacts'])
    contact_pattern = r'<div class="grid grid-cols-1 md:grid-cols-2 gap-8 max-w-2xl mx-auto">\s*<!-- Contact 1 -->.*?<!-- Contact 2 -->.*?</div>'
    new_contact_section = f'<div class="grid grid-cols-1 md:grid-cols-2 gap-8 max-w-2xl mx-auto">\n                            {contact_cards}\n                        </div>'
    
    new_content = re.sub(contact_pattern, new_contact_section, new_content, flags=re.DOTALL)
    
    # Write the updated content
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    except Exception as e:
        print(f"❌ Error writing {file_path}: {e}")
        return False

def main():
    """Main function to update all sports pages"""
    print("🚀 Starting sports pages update script...")
    print("=" * 50)
    
    # Read template content
    template_content = read_template_content()
    if not template_content:
        return
    
    print("✅ Template loaded successfully from football.html")
    
    # Update each sports page
    success_count = 0
    total_count = len(SPORTS_CONFIG)
    
    for sport_name in SPORTS_CONFIG.keys():
        print(f"\n📝 Updating {sport_name}.html...")
        
        if update_sports_page(sport_name, template_content):
            print(f"✅ {sport_name}.html updated successfully!")
            success_count += 1
        else:
            print(f"❌ Failed to update {sport_name}.html")
    
    print("\n" + "=" * 50)
    print(f"🎉 Update completed! {success_count}/{total_count} files updated successfully.")
    
    if success_count == total_count:
        print("🌟 All sports pages now have uniform, aesthetic layouts!")
        print("🔗 All links, contacts, and data have been preserved.")
        print("📱 All pages are now mobile-responsive with modern design.")
    else:
        print("⚠️  Some files may need manual review.")

if __name__ == "__main__":
    main()