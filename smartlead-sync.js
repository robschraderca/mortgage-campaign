// SmartLead Campaign Synchronization
// This ensures email sequences are always up-to-date in SmartLead

const SMARTLEAD_CAMPAIGN_IDS = {
    dentist: null,    // TODO: Set your SmartLead campaign ID
    restaurant: null, // TODO: Set your SmartLead campaign ID
    salon: null       // TODO: Set your SmartLead campaign ID
};

async function syncEmailSequenceToSmartLead() {
    const campaignId = SMARTLEAD_CAMPAIGN_IDS[campaignName];
    
    if (!campaignId) {
        console.log(`⚠️ SmartLead campaign ID not configured for ${campaignName}`);
        return;
    }
    
    console.log(`🔄 Syncing ${campaignName} campaign to SmartLead...`);
    
    // Collect current email sequence
    const emailSequence = [];
    
    for (let i = 1; i <= 5; i++) {
        const subjectInput = document.getElementById(`subject-${i}-input`);
        const bodyInput = document.getElementById(`body-${i}-input`);
        
        if (subjectInput && bodyInput) {
            // Email timing configuration
            const delays = [0, 2, 4, 5, 7]; // Days: 0, 2, 6, 11, 18
            
            emailSequence.push({
                seq_number: i,
                seq_delay_details: {
                    delay_in_days: delays[i - 1]
                },
                variant_distribution_type: "MANUAL_EQUAL",
                winning_metric_property: "REPLY_RATE",
                lead_distribution_percentage: 100,
                seq_variants: [{
                    variant_label: `Email ${i}`,
                    subject: subjectInput.value,
                    email_body: bodyInput.value,
                    variant_distribution_percentage: 100
                }]
            });
        }
    }
    
    try {
        // Call SmartLead API to update sequence
        // Uncomment when ready to use
        /*
        const response = await smartlead_save_campaign_sequence({
            campaign_id: campaignId,
            sequence: emailSequence
        });
        
        console.log('✅ Campaign synced to SmartLead successfully');
        showSmartLeadNotification('✅ Email sequence synced to SmartLead!', 'success');
        */
        
        // For now, just log what would be synced
        console.log('📧 Email sequence ready to sync:', emailSequence);
        console.log('💡 To enable: Set campaign ID and uncomment API call');
        
    } catch (error) {
        console.error('❌ Failed to sync to SmartLead:', error);
        showSmartLeadNotification(`❌ Sync failed: ${error.message}`, 'error');
    }
}

// Auto-sync when page loads
function initSmartLeadSync() {
    const campaignId = SMARTLEAD_CAMPAIGN_IDS[campaignName];
    
    if (campaignId) {
        // Sync after a short delay to ensure DOM is ready
        setTimeout(() => {
            syncEmailSequenceToSmartLead();
        }, 1000);
    }
}

// Manual sync button functionality
function manualSyncToSmartLead() {
    syncEmailSequenceToSmartLead();
}
