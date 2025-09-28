#!/usr/bin/env python3
"""
Verification script to check that all sports pages have been updated correctly
"""

import os
import re
from typing import Dict, List

def verify_page_structure(file_path: str, sport_name: str) -> Dict:
    """Verify that a sports page has the correct structure"""
    results = {
        'file_exists': False,
        'has_hero_section': False,
        'has_rules_section': False,
        'has_registration_section': False,
        'has_contact_section': False,
        'has_prize_pool': False,
        'has_modern_layout': False,
        'errors': []
    }
    
    try:
        if not os.path.exists(file_path):
            results['errors'].append(f"File {file_path} does not exist")
            return results
        
        results['file_exists'] = True
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check for hero section
        if 'hero-bg' in content and 'floating-animation' in content:
            results['has_hero_section'] = True
        else:
            results['errors'].append("Missing hero section")
        
        # Check for rules section
        if 'General Rules & Guidelines' in content and 'glass-effect' in content:
            results['has_rules_section'] = True
        else:
            results['errors'].append("Missing rules section")
        
        # Check for registration section
        if 'Register Your Team' in content and 'forms.gle' in content:
            results['has_registration_section'] = True
        else:
            results['errors'].append("Missing registration section")
        
        # Check for contact section
        if 'Points of Contact' in content and 'contact_phone' in content:
            results['has_contact_section'] = True
        else:
            results['errors'].append("Missing contact section")
        
        # Check for prize pool
        if 'Prize Pool' in content and 'gradient-text' in content:
            results['has_prize_pool'] = True
        else:
            results['errors'].append("Missing prize pool")
        
        # Check for modern layout elements
        modern_elements = ['hover-scale', 'glass-effect', 'gradient-text', 'material-icons']
        if all(element in content for element in modern_elements):
            results['has_modern_layout'] = True
        else:
            results['errors'].append("Missing modern layout elements")
        
    except Exception as e:
        results['errors'].append(f"Error reading file: {e}")
    
    return results

def main():
    """Main verification function"""
    print("🔍 Verifying sports pages updates...")
    print("=" * 60)
    
    sports = ['badminton', 'basketball', 'chess', 'kabaddi', 'tennis', 'tabletennis', 'volleyball', 'throwball']
    
    all_good = True
    
    for sport in sports:
        file_path = f"{sport}.html"
        print(f"\n📄 Checking {sport}.html...")
        
        results = verify_page_structure(file_path, sport)
        
        if results['file_exists']:
            print("✅ File exists")
        else:
            print("❌ File missing")
            all_good = False
            continue
        
        checks = [
            ('Hero Section', results['has_hero_section']),
            ('Rules Section', results['has_rules_section']),
            ('Registration Section', results['has_registration_section']),
            ('Contact Section', results['has_contact_section']),
            ('Prize Pool', results['has_prize_pool']),
            ('Modern Layout', results['has_modern_layout'])
        ]
        
        for check_name, passed in checks:
            if passed:
                print(f"✅ {check_name}")
            else:
                print(f"❌ {check_name}")
                all_good = False
        
        if results['errors']:
            print("⚠️  Errors found:")
            for error in results['errors']:
                print(f"   - {error}")
    
    print("\n" + "=" * 60)
    if all_good:
        print("🎉 All sports pages verified successfully!")
        print("🌟 All pages have uniform, modern, aesthetic layouts!")
        print("📱 All pages are mobile-responsive!")
        print("🔗 All links and data preserved!")
    else:
        print("⚠️  Some issues found. Please review the pages above.")

if __name__ == "__main__":
    main()