# SmartLead Auto-Sync Configuration

This feature automatically syncs your email sequences to SmartLead campaigns every time you load a campaign review page.

## 🎯 What It Does

**On Page Load:**
1. Reads all 5 emails from the current campaign
2. Formats them for SmartLead API
3. Syncs to your SmartLead campaign
4. Updates the email sequence automatically

**Manual Sync:**
- Orange "🔄 Sync to SmartLead" button in header
- Click anytime to force sync

## ⚙️ Configuration

### Step 1: Get Your SmartLead Campaign IDs

1. Log into SmartLead
2. Go to Campaigns
3. Note the campaign ID for each:
   - Dentist Campaign ID
   - Restaurant Campaign ID
   - Salon Campaign ID

### Step 2: Configure Each Campaign File

Edit each campaign file (dentist-review.html, restaurant-review.html, salon-review.html):

**Find this section:**
```javascript
const SMARTLEAD_CAMPAIGN_IDS = {
    dentist: null,    // TODO: Set your SmartLead campaign ID
    restaurant: null, // TODO: Set your SmartLead campaign ID
    salon: null       // TODO: Set your SmartLead campaign ID
};
```

**Update with your IDs:**
```javascript
const SMARTLEAD_CAMPAIGN_IDS = {
    dentist: 12345,      // Your actual campaign ID
    restaurant: 12346,   // Your actual campaign ID
    salon: 12347         // Your actual campaign ID
};
```

### Step 3: Enable API Calls

In each campaign file, find and **uncomment** this section:

```javascript
// Uncomment when ready to use
/*
const response = await smartlead_save_campaign_sequence({
    campaign_id: campaignId,
    sequence: emailSequence
});

console.log('✅ Campaign synced to SmartLead successfully');
showSmartLeadNotification('✅ Email sequence synced to SmartLead!', 'success');
*/
```

**Change to:**
```javascript
const response = await smartlead_save_campaign_sequence({
    campaign_id: campaignId,
    sequence: emailSequence
});

console.log('✅ Campaign synced to SmartLead successfully');
showSmartLeadNotification('✅ Email sequence synced to SmartLead!', 'success');
```

## 📧 Email Sequence Timing

The sync automatically sets these delays:

| Email | Day Sent | Delay |
|-------|----------|-------|
| Email 1 | Day 0 | Immediate |
| Email 2 | Day 2 | 2 days after Email 1 |
| Email 3 | Day 6 | 4 days after Email 2 |
| Email 4 | Day 11 | 5 days after Email 3 |
| Email 5 | Day 18 | 7 days after Email 4 |

**Total Campaign Duration:** 18 days

## 🔄 How Syncing Works

### Automatic Sync (On Page Load)
1. Page loads → Wait 1 second
2. Check if campaign ID is configured
3. If yes: Collect all email data
4. Format for SmartLead API
5. Call `smartlead_save_campaign_sequence`
6. Show success/error notification

### Manual Sync (Button Click)
1. Click "🔄 Sync to SmartLead" button
2. Same process as automatic sync
3. Use this after editing emails

## 📋 What Gets Synced

For each email:
- ✅ Subject line (current version)
- ✅ Email body (current version with edits)
- ✅ Sequence number (1-5)
- ✅ Delay timing
- ✅ Variant configuration
- ❌ Comments (not synced)

## 🎨 Visual Feedback

**Success:**
- Green notification: "✅ Email sequence synced to SmartLead!"
- Console log: "✅ Campaign synced to SmartLead successfully"

**Not Configured:**
- Console log: "⚠️ SmartLead campaign ID not configured"

**Error:**
- Red notification: "❌ Sync failed: [error message]"
- Console error with details

## 🧪 Testing

### Before Enabling API:
1. Open browser console (F12)
2. Load a campaign page
3. Look for: "📧 Email sequence ready to sync"
4. Review the data structure
5. Verify all emails are included

### After Enabling API:
1. Load campaign page
2. Check for success notification
3. Go to SmartLead dashboard
4. Verify email sequence updated
5. Check timing/delays are correct

## 🚨 Troubleshooting

**"Campaign ID not configured"**
- Set SMARTLEAD_CAMPAIGN_IDS in the file
- Must be a number, not string

**"Sync failed"**
- Check SmartLead API credentials
- Verify campaign ID exists
- Check browser console for details
- Ensure MCP server is running

**Emails not updating**
- Hard refresh page (Ctrl+Shift+R)
- Check if API call is uncommented
- Verify campaign ID is correct
- Check SmartLead campaign status

**Button not visible**
- Clear browser cache
- Check if page loaded completely
- Look in header below campaign title

## 💡 Best Practices

1. **Test First**: Use console logging before enabling API
2. **Verify IDs**: Double-check campaign IDs are correct
3. **Edit Then Sync**: Make email changes, then click sync button
4. **Check SmartLead**: Always verify in SmartLead dashboard
5. **Keep Backup**: Save email sequences before syncing

## 🔐 Security Notes

- Campaign IDs are stored client-side
- API calls use MCP server for authentication
- No API keys exposed in browser
- All data encrypted in transit

## 📊 Sync Status

Check browser console for:
- `🔄 Syncing [campaign] to SmartLead...`
- `✅ Campaign synced successfully`
- `📧 Email sequence ready to sync: [data]`

## 🆘 Support

Issues? Check:
1. Browser console for errors
2. SmartLead API status
3. Campaign ID configuration
4. MCP server connection

---

**Version:** 1.0  
**Last Updated:** 2025-01-XX  
**Feature:** Auto-sync on page load + Manual sync button
