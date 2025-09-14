# **Workshop Booking**

> This website is for coordinators to book a workshop(s), they can book a workshop based on instructors posts or can propose a workshop date based on their convenience.


### Features
* Statistics
    1. Instructors Only
        * Monthly Workshop Count
        * Instructor/Coordinator Profile stats
        * Upcoming Workshops
        * View/Post comments on Coordinator's Profile
    2. Open to All
        * Workshops taken over Map of India
        * Pie chart based on Total Workshops taken to Type of Workshops.

* Workshop Related Features
    > Instructors can Accept, Reject or Delete workshops based on their preference, also they can postpone a workshop based on coordinators request.

__NOTE__: Check docs/Getting_Started.md for more info.

---

## UI/UX Modernization (2025 Update)

Recent improvements focus on mobile-first access for students and coordinators:

### What Changed
* Added meta viewport + Bootstrap 5 (layered over existing Bootstrap 4 assets for backward compatibility).
* Introduced a mobile-friendly, accessible navigation bar with semantic landmarks (`<main>`, `<nav>`, `<footer>`).
* Added skip link for keyboard / screen reader users.
* Created `responsive.css` with:
    * Fluid typography (`clamp()`).
    * Responsive table stacking pattern (data-label attribute approach).
    * Improved pagination wrapping + tap target sizing.
    * Reduced-motion + dark-mode readiness (`data-theme="dark"`).
* Footer consistency + automatic current year.
* Accessibility: focus-visible styles, ARIA labels, landmark roles.

### Design Principles Applied
1. Mobile First: Layout spacing and font scaling tuned for small screens; enhancements progressively layered for larger viewports.
2. Progressive Enhancement: Legacy CSS/JS retained to avoid regressions; new layer is additive, not destructive.
3. Accessibility: Semantic landmarks, skip link, focus rings, logical nav structure, larger interactive areas.
4. Readability & Scan-ability: Max readable line length utility, improved heading rhythm, consistent spacing utilities.
5. Performance Awareness: Minimal custom CSS (~4 KB), CDN bootstrap cached widely, deferred legacy scripts.

### Ensuring Responsiveness
* Viewport meta added.
* Used flex + wrap for pagination and nav items.
* Tables collapse into stacked cards under 640px using generated labels.
* Clamp-based typography scales smoothly between small and medium devices.
* Tap-friendly targets for touch devices (≥44px height where possible).

### Trade-offs
| Area | Decision | Trade-off |
|------|----------|-----------|
| Dual Bootstrap (4 local + 5 CDN) | Kept both temporarily | Slight CSS bloat; mitigated by caching and small file sizes. |
| No heavy JS framework | Lean footprint | Limited interactivity upgrades (future: React/Vue optional). |
| Table stacking via CSS only | Zero JS overhead | Requires template additions (data-label) for full adoption on all tables. |
| Dark mode opt-in only | Avoids user surprise | Requires future toggle UI. |

### Most Challenging Part
Balancing upgrade scope with backwards compatibility. Approach: additive layering (new Bootstrap via CDN) and conservative overrides in `responsive.css` to avoid breaking legacy templates.

### Next Suggested Enhancements
* Add automated Lighthouse + axe accessibility checks in CI.
* Provide dark mode toggle storing preference in `localStorage`.
* Refactor duplicated navigation logic into an include.
* Migrate fully to Bootstrap 5 and drop legacy bundle after regression audit.

---

## Design Rationale (Q & A)

**Q: What design principles guided your improvements?**  
**A:** The redesign followed five core principles: (1) Mobile-first layout with fluid typography and touch-friendly hit targets; (2) Progressive enhancement—new Bootstrap 5 + modern JS layered without breaking legacy Bootstrap 4 templates; (3) Accessibility—semantic landmarks, skip link, improved focus states, ARIA-conscious component structure; (4) Consistency & readability—consolidated spacing rhythm, card/table visual hierarchy, clear status badges; (5) Performance mindfulness—minimal custom CSS, deferring heavy behavior, and reusing CDN‑cached libraries.

**Q: How did you ensure responsiveness across devices?**  
**A:** Applied a `meta viewport`, used flexbox/grid utility classes instead of fixed widths, introduced `clamp()` for scalable typography, created a CSS-only table stacking pattern for narrow viewports, ensured nav collapses gracefully, and verified interactive elements meet recommended 44px tap area. Media-queries were kept minimal—most adjustments rely on intrinsic layout + utility classes.

**Q: What trade-offs did you make between the design and performance?**  
**A:** Key trade-offs: temporarily shipping dual Bootstrap versions (slight CSS overhead) to avoid refactoring fragile legacy templates; choosing a lightweight enhancement stack (HTMX + Flatpickr + Chart.js) instead of a heavier SPA framework (sacrificing advanced client-side state features); using client-side date/chart libraries for UX despite extra KBs (offset by CDN caching); postponing removal of jQuery UI until Flatpickr stability is confirmed to reduce regression risk.

**Q: What was the most challenging part of the task and how did you approach it?**  
**A:** The hardest challenge was modernizing UX while preserving legacy template behavior. The approach: inventory existing dependencies, add new layers in a non-destructive order (CSS variables, responsive helpers, then Bootstrap 5), isolate risky changes (navigation, workshop status views) behind conditional logic, and introduce defensive coding (missing profile handling + auto profile signals) to prevent runtime errors that could undermine UX gains. This phased layering let us ship incremental improvements with fast rollback capability.


---

## Setup Instructions

### 1. Clone Repository
```bash
git clone https://github.com/<your-username>/workshop_booking.git
cd workshop_booking
```

### 2. Create Conda Environment (Recommended)
```bash
conda create -n workshop_booking python=3.11 -y
conda activate workshop_booking
```

### 3. Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Local Environment Config
If needed copy `local_settings.py` example or adjust database/email settings.

### 5. Run Migrations
```bash
python manage.py migrate
```

### 6. Create Superuser (optional)
```bash
python manage.py createsuperuser
```

### 7. Run Development Server
```bash
python manage.py runserver
```
Visit: http://127.0.0.1:8000/

### 7.a (Optional) Seed Initial CMS Content
Automatically create a default home page and Home nav item:
```bash
python manage.py seed_initial_content
```
Safe to re-run; it will not duplicate entries.

### 8. Collect Static (Production Deploy)
```bash
python manage.py collectstatic
```

### 9. Tests
```bash
python manage.py test
```

### 10. Dark Mode (Optional)
Add `data-theme="dark"` to `<html>` manually or via script (future toggle recommended).

---

## Screenshots

Place your captured images in `docs/screenshots/`. Filenames below are suggested; adjust if needed. Use consistent viewport width (~1440px desktop) and a mobile width (~375–414px) for before/after comparisons.

### Core Before / After (Responsiveness & Navigation)
```

All the screenshots are in the docs\screenshots
```

### Capture Guidelines
1. Clear test data for “empty state” screenshots (as shown in dashboard welcome).
2. Use a neutral browser zoom (100%).
3. For mobile versions: open DevTools device toolbar (e.g., 375x812 iPhone X) before capturing.
4. Ensure the theme toggle reflects the mode being captured (moon = ready for dark, sun = currently dark depending on icon logic).
5. Commit images using lossless PNG or optimized WebP (keep text crisp). Avoid > 300KB per image where possible.


---

## Contribution Workflow
1. Create a feature branch: `git checkout -b feature/responsive-ui`
2. Commit in logical chunks with meaningful messages.
3. Open a Pull Request (if collaborating) or merge locally.

---

## License
See `LICENSE` file.

---

## Troubleshooting

### RelatedObjectDoesNotExist: User has no profile
If you attempt to log in and encounter an error `User has no profile`, the Django `User` row was created without the corresponding `Profile` (e.g. via `createsuperuser` or an old database import). The application now handles this gracefully, but you still need to create the profile record.

Choose one of the following fixes:

1. Re-register the account (simplest for dev/testing):
    * Visit `/workshop/register/` and submit the form. (If the username/email already exists, delete the user first in admin.)

2. Create a Profile in Django admin:
    * Go to `/admin/` -> Profiles -> Add.
    * Pick the existing user and fill required fields: institute, department, phone number (10 digits), state, position.
    * Save. Re-attempt login.

3. Create via Django shell:
    ```python
    python manage.py shell
    >>> from django.contrib.auth.models import User
    >>> from workshop_app.models import Profile
    >>> from django.utils import timezone
    >>> u = User.objects.get(username='your_username')
    >>> Profile.objects.create(
    ...     user=u,
    ...     institute='Your Institute',
    ...     department='computer engineering',
    ...     phone_number='9999999999',
    ...     position='coordinator',
    ...     how_did_you_hear_about_us='Google',
    ...     location='City',
    ...     state='IN-MH',
    ...     is_email_verified=True,  # or False to go through activation
    ...     activation_key='manual',
    ...     key_expiry_time=timezone.now() + timezone.timedelta(days=1),
    ... )
    ```

4. Bulk repair missing profiles (management command example):
    ```python
    from django.core.management.base import BaseCommand
    from django.contrib.auth.models import User
    from workshop_app.models import Profile
    from django.utils import timezone

    class Command(BaseCommand):
         help = 'Create placeholder profiles for users missing one.'

         def handle(self, *args, **options):
              created = 0
              for u in User.objects.all():
                    if not hasattr(u, 'profile'):
                         Profile.objects.create(
                              user=u,
                              institute='Placeholder Institute',
                              department='computer engineering',
                              phone_number='9999999999',
                              position='coordinator',
                              how_did_you_hear_about_us='Google',
                              location='City',
                              state='IN-MH',
                              is_email_verified=True,
                              activation_key='bulk',
                              key_expiry_time=timezone.now() + timezone.timedelta(days=1),
                         )
                         created += 1
              self.stdout.write(self.style.SUCCESS(f'Created {created} profiles'))
    ```

After adding the profile, retry login. If you want the activation flow, set `is_email_verified=False`.

---

## Optional UI Enhancements (2025 Additions)

This project now includes several progressive UI improvements. All are loosely coupled so you can opt-out individually.

### Summary Table
| Feature | Location / Entry | Disable By | Notes |
|---------|------------------|------------|-------|
| Dark Mode Toggle | `workshop_app/base.html` theme button + CSS vars in `base.css` | Remove toggle button + leave `data-theme="light"` | Persists preference in `localStorage`.
| Toast Notifications (Accessible) | JS block in `workshop_app/base.html` | Remove `showToast` script OR drop `toastr.min.js` | Falls back to inline alerts if toastr missing.
| Flatpickr Date Picker | Auto-init script in `workshop_app/base.html` | Remove Flatpickr `<script>` & `<link>` tags | Keeps native `<input type=date>`.
| HTMX Accept Workshop | Accept button in `workshop_status_instructor.html` + partial + view branch | Replace button with original anchor + remove htmx script | Partial template: `partials/accepted_row.html`.
| Chart.js Modern Config | `statistics_app/workshop_public_stats.html` | Revert to previous inline script and older CDN | Uses v4 UMD build.

### Dark Mode
* Theme variables defined in `workshop_app/static/workshop_app/css/base.css`.
* Toggle logic updates `<html data-theme>` and stores value under `theme` key.
* To force dark for all users: set `<html data-theme="dark">` and delete the toggle button.

### Toastr Wrapper
* Function: `showToast(level, message)` – levels map to `success`, `info`, `warning`, `error`.
* ARIA live region fallback ensures messages still announced if library removed.
* To disable globally without editing templates: delete `workshop_app/static/workshop_app/js/toastr.min.js` and the wrapper will degrade silently.

### Flatpickr Integration
* Targets: All `input[type=date]` and any element with class `.js-date`.
* Date format: submits ISO (`Y-m-d`), displays friendly `d M Y` via `altInput`.
* If you have server-side validation relying on original widget, no change needed.

### HTMX Enhancement (Accept Workshop Action)
* Accept button issues an `hx-post` to the existing view.
* View inspects `HX-Request` header and renders partial `accepted_row.html`.
* Fallback: If JS disabled, nothing happens (consider adding a `<noscript>` anchor for progressive enhancement later).

### Updated Chart.js Usage
* Migrated to Chart.js v4; logic wrapped in an IIFE for isolation.
* Accessible canvas receives `role="img"` and descriptive `aria-label`.
* To revert: swap back the old CDN and restore previous inline script structure.

### Removing/Opting Out Quickly
| Scenario | Minimal Action |
|----------|----------------|
| Remove all enhancements | Delete added CDN lines & new script block sections in `base.html`; keep legacy assets only. |
| Keep dark mode only | Remove Flatpickr + HTMX + Chart.js CDN lines; leave theme toggle + CSS vars. |
| Only keep interactivity (HTMX) | Remove Flatpickr & Chart.js; leave htmx + partial + accept button. |

### Future Ideas (Not Yet Implemented)
* Noscript fallback for HTMX buttons.
* Replace jQuery UI remnants fully once Flatpickr validated everywhere.
* DRY navigation includes across CMS and workshop base templates.
* Automated visual regression tests (Playwright + CI artifacts).

---
## Maintenance Tips
1. Audit bundle weight occasionally (e.g., use browser DevTools Coverage) before adding further libraries.
2. When ready, consider removing legacy Bootstrap 4 assets and standardizing on Bootstrap 5 or a utility framework.
3. If migrating to Tailwind or similar, keep the CSS variables layer so dark mode logic survives the transition.

---

## Changelog (Key Recent UI Changes)

| Date (YYYY-MM-DD) | Change | Files / Areas | Notes |
|-------------------|--------|---------------|-------|
| 2025-09-14 | Added dark theme form + table styling (statistics filters, cards, jumbotrons) | `base.css` | Improves readability in dark mode (contrast for inputs, card headers, table rows). |
| 2025-09-14 | HTMX partial accept workflow for instructor | `workshop_status_instructor.html`, `partials/accepted_row.html`, `views.accept_workshop` | Inline update without full page reload; safe fallback if JS disabled. |
| 2025-09-14 | Flatpickr enhancement auto-init | `base.html` | Progressive enhancement for date inputs; retains native date inputs if script missing. |
| 2025-09-14 | Chart.js v4 refactor (accessible modal) | `statistics_app/workshop_public_stats.html` | Responsive chart, better color scheme, accessible canvas. |
| 2025-09-14 | Dark mode toggle + CSS variables | `base.html`, `base.css` | LocalStorage persistence; future theming foundation. |
| 2025-09-14 | Accessible toast wrapper | `base.html` | ARIA live region fallback if toastr absent. |
| 2025-09-14 | Auto profile creation signals | `signals.py`, `apps.py` | Prevents RelatedObjectDoesNotExist for `user.profile`. |

For earlier modernization details see the “UI/UX Modernization (2025 Update)” section above.


