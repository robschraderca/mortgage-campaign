# Campaign Review Template - Standard Features

This document defines the standard features that MUST be included in every campaign review page.

## Standard Features (All Campaigns)

### 1. **Page Structure**
- Professional gradient header with campaign icon and title
- Campaign overview section with 4 info cards
- 5 email cards with consistent styling
- Approval section at bottom

### 2. **Each Email Card Must Have**
- Email number and title in header
- Timing badge (Day X)
- Subject line section with "← Edit Subject" label
- Body copy section with "← Edit Body Copy" label
- Signature section
- Comments & Feedback section (always visible)
- Edit controls with 6 buttons:
  - ✏️ Edit Email
  - 💾 Save Changes (hidden by default)
  - ↩️ Restore Original (hidden by default)
  - ✖️ Cancel (hidden by default)
  - ✓ Approve (individual email)
  - ✗ Deny (individual email)

### 3. **Comments Section**
- Always visible textarea
- Submit Comment button
- "✓ Comment Saved" indicator
- Saves independently from email edits
- Persists across sessions

### 4. **Individual Email Approval**
- Each email has approve/deny buttons
- Toggle functionality (click again to remove)
- Visual feedback (fills with color when active)
- Saves to localStorage independently

### 5. **Campaign-Level Approval**
- Three buttons at bottom:
  - ✓ APPROVE CAMPAIGN
  - ✗ DENY CAMPAIGN
  - ↺ UNAPPROVE CAMPAIGN
- Professional outline style
- Status badge display
- Confirmation dialogs

### 6. **Navigation**
- Back to All Campaigns button
- Logout button
- Both fixed in top-right corner

### 7. **Data Persistence**
- All edits saved to localStorage
- Comments saved separately
- Individual email approvals tracked
- Campaign-level decision tracked
- Loads on page refresh

### 8. **Styling Standards**
- Inter font family
- Gradient backgrounds (#667eea to #764ba2)
- White cards with shadows
- Hover effects on all buttons
- Responsive design
- Professional color scheme:
  - Green for approve (#38a169)
  - Red for deny (#e53e3e)
  - Orange for comments (#ed8936)
  - Gray for neutral (#718096)

## Campaign-Specific Customizations

### Required Updates for Each New Campaign
1. Campaign icon (emoji in header)
2. Campaign name (title and JavaScript variable)
3. Target audience description
4. All 5 email subjects
5. All 5 email bodies
6. Confirmation message texts
7. Email 1 signature: "Thanks, Michael"
8. Emails 2-5 signature: "Michael"

## File Naming Convention
- dentist-review.html
- restaurant-review.html
- salon-review.html
- [industry]-review.html

## localStorage Keys
- `campaign-edits` - All email edits
- `campaign-{name}` - Campaign decision
- `email-{name}-{num}` - Individual email decisions

## Future Enhancement Checklist
When adding new features to ANY campaign:
1. ✅ Update dentist-review.html
2. ✅ Update restaurant-review.html
3. ✅ Update salon-review.html
4. ✅ Update this template document
5. ✅ Test all three campaigns
6. ✅ Commit with clear message

## Current Template Version
**Version:** 2.0  
**Last Updated:** 2025-01-XX  
**Standard Features:** 11  
**Active Campaigns:** 3 (Dentist, Restaurant, Salon)
