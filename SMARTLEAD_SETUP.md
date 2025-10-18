# SmartLead Integration Setup

This document explains how to connect your campaign review system to SmartLead API.

## Overview

When all 5 emails in a campaign are approved, the system can automatically:
1. Notify you that the campaign is ready
2. Update the SmartLead campaign status to "START"
3. Launch your email sequence

## Configuration Steps

### 1. Get Your SmartLead Campaign IDs

1. Log into SmartLead
2. Navigate to your campaigns
3. Find the campaign ID for each campaign:
   - Dentist Campaign ID
   - Restaurant Campaign ID  
   - Salon Campaign ID

### 2. Update Campaign Files

For **each** campaign file (dentist-review.html, restaurant-review.html, salon-review.html):

1. Open the file
2. Find this line:
   ```javascript
   const SMARTLEAD_CAMPAIGN_ID = null;
   ```
3. Replace with your actual campaign ID:
   ```javascript
   const SMARTLEAD_CAMPAIGN_ID = 12345; // Your SmartLead campaign ID
   ```

### 3. Enable SmartLead API (Optional)

The system is currently set up to show notifications only. To enable actual API integration:

1. Uncomment the API call in each campaign file:
   ```javascript
   // Find this section:
   // try {
   //     const response = await smartlead_update_campaign_status({
   //         campaign_id: SMARTLEAD_CAMPAIGN_ID,
   //         status: 'START'
   //     });
   //     showSmartLeadNotification('✓ SmartLead campaign started successfully!', 'success');
   // } catch (error) {
   //     showSmartLeadNotification('⚠️ Error starting SmartLead campaign: ' + error.message, 'error');
   // }
   
   // Uncomment to enable:
   try {
       const response = await smartlead_update_campaign_status({
           campaign_id: SMARTLEAD_CAMPAIGN_ID,
           status: 'START'
       });
       showSmartLeadNotification('✓ SmartLead campaign started successfully!', 'success');
   } catch (error) {
       showSmartLeadNotification('⚠️ Error starting SmartLead campaign: ' + error.message, 'error');
   }
   ```

## How It Works

### Current Behavior (Without API Enabled)

When you approve emails:
- **Individual Email Approved**: Shows notification "Email X approved (X/5 emails approved)"
- **All 5 Emails Approved**: Shows notification "All emails approved! Campaign ready to launch in SmartLead."

### With API Enabled

When all 5 emails are approved:
1. System checks SmartLead campaign ID is configured
2. Calls SmartLead API to update campaign status to "START"
3. Your campaign begins sending automatically
4. Shows success/error notification

## Available SmartLead Functions

The MCP SmartLead integration provides these functions:

### Update Campaign Status
```javascript
smartlead_update_campaign_status({
    campaign_id: 123,
    status: 'START' // or 'PAUSED', 'STOPPED'
});
```

### Get Campaign Details
```javascript
smartlead_get_campaign({
    campaign_id: 123
});
```

### Update Campaign Settings
```javascript
smartlead_update_campaign_settings({
    campaign_id: 123,
    name: "Updated Campaign Name",
    settings: { /* your settings */ }
});
```

## Notifications

The system shows color-coded notifications:

- 🔵 **Blue (Info)**: Individual email approved, progress update
- 🟢 **Green (Success)**: All emails approved or API success
- 🔴 **Red (Error)**: API error or failure

Notifications appear in the top-right corner and auto-dismiss after 5 seconds.

## Testing

To test the integration:

1. Configure campaign IDs in all three files
2. Approve all 5 emails in a campaign
3. Check the notification that appears
4. (Optional) Check SmartLead dashboard to verify campaign started

## Troubleshooting

**Notifications not appearing:**
- Check browser console for errors
- Verify SMARTLEAD_CAMPAIGN_ID is set

**API calls failing:**
- Verify SmartLead API credentials
- Check campaign ID is correct
- Ensure MCP SmartLead server is running

**Campaign not starting:**
- Verify all 5 emails are approved (check localStorage)
- Check SmartLead campaign is in correct initial state
- Review error messages in notifications

## Security Notes

- Campaign IDs are stored in HTML files (client-side)
- No sensitive API keys are exposed in browser
- API calls use MCP server for authentication
- All communication happens through secure channels

## Support

For issues with:
- **This integration**: Check browser console logs
- **SmartLead API**: Contact SmartLead support
- **MCP Server**: Check MCP documentation

---

**Version:** 1.0  
**Last Updated:** 2025-01-XX  
**Status:** Ready for configuration
