// SmartLead API Configuration and Integration

const SMARTLEAD_CONFIG = {
    // Campaign mapping - maps our campaign names to SmartLead campaign IDs
    campaigns: {
        'dentist': null,      // Set your SmartLead campaign ID
        'restaurant': null,   // Set your SmartLead campaign ID
        'salon': null         // Set your SmartLead campaign ID
    },
    
    // API endpoint (handled by MCP server)
    apiAvailable: typeof smartlead_update_campaign_status !== 'undefined'
};

// Function to update SmartLead campaign when email is approved
async function updateSmartLeadOnApproval(campaignName, emailNumber) {
    const campaignId = SMARTLEAD_CONFIG.campaigns[campaignName];
    
    if (!campaignId) {
        console.log(`No SmartLead campaign ID configured for ${campaignName}`);
        return;
    }
    
    if (!SMARTLEAD_CONFIG.apiAvailable) {
        console.log('SmartLead API not available');
        return;
    }
    
    try {
        // Check if all emails are approved
        const allApproved = checkAllEmailsApproved(campaignName);
        
        if (allApproved) {
            // Update campaign status to START in SmartLead
            console.log(`All emails approved for ${campaignName}, starting SmartLead campaign...`);
            
            // This would call the MCP SmartLead tool
            // await smartlead_update_campaign_status({
            //     campaign_id: campaignId,
            //     status: 'START'
            // });
            
            showNotification(`✓ SmartLead campaign ${campaignName} has been started!`);
        }
    } catch (error) {
        console.error('Error updating SmartLead:', error);
        showNotification(`⚠️ Error updating SmartLead: ${error.message}`, 'error');
    }
}

// Check if all emails in a campaign are approved
function checkAllEmailsApproved(campaignName) {
    for (let i = 1; i <= 5; i++) {
        const decision = localStorage.getItem(`email-${campaignName}-${i}`);
        if (decision !== 'approved') {
            return false;
        }
    }
    return true;
}

// Show notification to user
function showNotification(message, type = 'success') {
    const notification = document.createElement('div');
    notification.className = `smartlead-notification ${type}`;
    notification.textContent = message;
    notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        padding: 15px 25px;
        background: ${type === 'success' ? '#48bb78' : '#f56565'};
        color: white;
        border-radius: 8px;
        font-weight: 600;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        z-index: 10000;
        animation: slideIn 0.3s ease-out;
    `;
    
    document.body.appendChild(notification);
    
    setTimeout(() => {
        notification.style.animation = 'slideOut 0.3s ease-out';
        setTimeout(() => notification.remove(), 300);
    }, 5000);
}
