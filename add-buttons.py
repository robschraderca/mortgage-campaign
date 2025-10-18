import re

campaigns = {
    'dentist': {
        'icon': '🦷',
        'name': 'Dentist',
        'title': 'Dentist Campaign Review'
    },
    'restaurant': {
        'icon': '🍽️',
        'name': 'Restaurant',
        'title': 'Restaurant Campaign Review'
    },
    'salon': {
        'icon': '💇',
        'name': 'Salon',
        'title': 'Salon Campaign Review'
    }
}

for campaign_id, campaign_info in campaigns.items():
    filename = f'{campaign_id}-review.html'
    
    with open(filename, 'r') as f:
        content = f.read()
    
    # 1. Add CSS for buttons before DARK THEME OVERLAY
    button_css = '''
        /* Export and Copy Buttons */
        .header-actions {
            display: flex;
            gap: 15px;
            align-items: center;
            flex-wrap: wrap;
        }
        
        .btn-copy-emails {
            padding: 12px 28px;
            background: linear-gradient(135deg, #48bb78 0%, #38a169 100%);
            border: none;
            border-radius: 10px;
            color: white;
            font-weight: 600;
            font-size: 0.95em;
            cursor: pointer;
            transition: all 0.3s;
            display: inline-flex;
            align-items: center;
            gap: 10px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            box-shadow: 0 4px 15px rgba(72, 187, 120, 0.3);
            white-space: nowrap;
        }
        
        .btn-copy-emails:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 25px rgba(72, 187, 120, 0.4);
        }
        
        .btn-copy-emails.copied {
            background: linear-gradient(135deg, #4299e1 0%, #3182ce 100%);
        }
        
        .btn-export-pdf-header {
            padding: 12px 28px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border: none;
            border-radius: 10px;
            color: white;
            font-weight: 600;
            font-size: 0.95em;
            cursor: pointer;
            transition: all 0.3s;
            display: inline-flex;
            align-items: center;
            gap: 10px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
            white-space: nowrap;
        }
        
        .btn-export-pdf-header:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
        }
        
'''
    
    if '/* DARK THEME OVERLAY */' in content:
        content = content.replace('        /* DARK THEME OVERLAY */', button_css + '        /* DARK THEME OVERLAY */')
    
    # 2. Add HTML buttons in header (find the nav-buttons section and add before it)
    buttons_html = '''            <div class="header-actions">
                <button class="btn-copy-emails" onclick="copyEmailsToClipboard()">
                    <span>📋</span>
                    <span>Copy Emails</span>
                </button>
                <button class="btn-export-pdf-header" onclick="exportToPDF()">
                    <span>📥</span>
                    <span>Export PDF</span>
                </button>
            </div>
            
'''
    
    # Insert before nav-buttons
    content = content.replace(
        '        <div class="nav-buttons">',
        buttons_html + '        <div class="nav-buttons">'
    )
    
    # 3. Add JavaScript functions before the init function
    js_functions = '''        // Copy Emails to Clipboard
        async function copyEmailsToClipboard() {
            const campaignTitle = document.querySelector('.header h1').textContent;
            const campaignSubtitle = document.querySelector('.header p').textContent;
            
            let emailsText = `${campaignTitle}\\n${campaignSubtitle}\\n`;
            emailsText += '='.repeat(80) + '\\n\\n';
            
            for (let i = 1; i <= 5; i++) {
                const subjectDisplay = document.getElementById(`subject-${i}-display`);
                const bodyDisplay = document.getElementById(`body-${i}-display`);
                const emailCard = subjectDisplay ? subjectDisplay.closest('.email-card') : null;
                
                if (emailCard && subjectDisplay && bodyDisplay) {
                    const emailTitle = emailCard.querySelector('h2').textContent;
                    const timing = emailCard.querySelector('.email-card > p').textContent;
                    
                    emailsText += `${emailTitle}\\n`;
                    emailsText += `${timing}\\n`;
                    emailsText += '-'.repeat(80) + '\\n\\n';
                    emailsText += `SUBJECT: ${subjectDisplay.textContent}\\n\\n`;
                    emailsText += `${bodyDisplay.textContent}\\n\\n`;
                    emailsText += '='.repeat(80) + '\\n\\n';
                }
            }
            
            try {
                await navigator.clipboard.writeText(emailsText);
                showCopyFeedback(true);
            } catch (err) {
                const textarea = document.createElement('textarea');
                textarea.value = emailsText;
                textarea.style.position = 'fixed';
                textarea.style.opacity = '0';
                document.body.appendChild(textarea);
                textarea.select();
                
                try {
                    document.execCommand('copy');
                    showCopyFeedback(true);
                } catch (err2) {
                    showCopyFeedback(false);
                }
                
                document.body.removeChild(textarea);
            }
        }
        
        function showCopyFeedback(success) {
            const btn = document.querySelector('.btn-copy-emails');
            if (!btn) return;
            
            const originalHTML = btn.innerHTML;
            
            if (success) {
                btn.classList.add('copied');
                btn.innerHTML = '<span>✓</span><span>Copied!</span>';
                alert('✓ Email sequence copied to clipboard!');
            } else {
                alert('⚠️ Failed to copy to clipboard');
            }
            
            setTimeout(() => {
                btn.classList.remove('copied');
                btn.innerHTML = originalHTML;
            }, 2000);
        }
        
        // Export to PDF
        function exportToPDF() {
            alert('PDF export feature - Use browser Print function (Ctrl+P / Cmd+P) and select "Save as PDF"');
        }
        
'''
    
    # Insert before init function
    content = content.replace(
        '        function init() {',
        js_functions + '        function init() {'
    )
    
    with open(filename, 'w') as f:
        f.write(content)
    
    print(f'✓ Added buttons to {filename}')

print('\nAll campaigns updated with copy and export buttons')
