/* IntrepidX Philosophy Limited — site behaviour (no dependencies) */
(function () {
  "use strict";

  var doc = document.documentElement;
  doc.classList.add("js");

  /* Header: solid background once the page is scrolled */
  var header = document.querySelector(".site-header");
  var toTop = document.querySelector(".to-top");
  function onScroll() {
    var y = window.scrollY || window.pageYOffset;
    if (header) header.classList.toggle("is-solid", y > 40);
    if (toTop) toTop.classList.toggle("is-visible", y > 700);
  }
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  /* Full-screen menu */
  var menu = document.getElementById("site-menu");
  var openBtn = document.querySelector("[data-menu-open]");
  var closeBtn = document.querySelector("[data-menu-close]");
  var lastFocus = null;

  function focusables() {
    return menu ? Array.prototype.slice.call(menu.querySelectorAll("a[href], button:not([disabled])")) : [];
  }
  function openMenu() {
    if (!menu) return;
    lastFocus = document.activeElement;
    menu.hidden = false;
    // allow the browser to register the un-hidden state before animating
    requestAnimationFrame(function () {
      menu.classList.add("is-open");
      document.body.classList.add("menu-open");
      if (openBtn) openBtn.setAttribute("aria-expanded", "true");
      var f = focusables();
      if (f.length) f[0].focus();
    });
  }
  function closeMenu() {
    if (!menu) return;
    menu.classList.remove("is-open");
    document.body.classList.remove("menu-open");
    if (openBtn) openBtn.setAttribute("aria-expanded", "false");
    window.setTimeout(function () { if (!menu.classList.contains("is-open")) menu.hidden = true; }, 420);
    if (lastFocus && lastFocus.focus) lastFocus.focus();
  }
  if (openBtn) openBtn.addEventListener("click", openMenu);
  if (closeBtn) closeBtn.addEventListener("click", closeMenu);
  if (menu) {
    menu.addEventListener("keydown", function (e) {
      if (e.key === "Escape") { closeMenu(); return; }
      if (e.key !== "Tab") return;
      var f = focusables();
      if (!f.length) return;
      var first = f[0], last = f[f.length - 1];
      if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
      else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
    });
    menu.addEventListener("click", function (e) {
      var a = e.target.closest ? e.target.closest("a[href]") : null;
      if (a && a.getAttribute("href").indexOf("#") !== -1) closeMenu();
    });
  }

  /* Reveal on scroll */
  var items = document.querySelectorAll("[data-reveal]");
  if ("IntersectionObserver" in window && items.length) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-in");
          io.unobserve(entry.target);
        }
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.08 });
    items.forEach(function (el) { io.observe(el); });
  } else {
    items.forEach(function (el) { el.classList.add("is-in"); });
  }

  /* Footer year */
  var year = document.querySelector("[data-year]");
  if (year) year.textContent = String(new Date().getFullYear());

  /* Contact form: compose an email in the visitor's mail app (no server needed) */
  var form = document.querySelector("[data-mail-form]");
  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      if (!form.reportValidity()) return;
      var get = function (n) { var el = form.elements[n]; return el ? el.value.trim() : ""; };
      var to = form.getAttribute("data-to") || "info@intrepidx.biz";
      var subject = get("subject") || "Enquiry from the website";
      var lines = [
        get("message"),
        "",
        "—",
        get("name"),
        get("organisation"),
        get("email"),
        get("phone")
      ].filter(function (l, i) { return i < 3 || l; });
      var href = "mailto:" + to + "?subject=" + encodeURIComponent(subject) + "&body=" + encodeURIComponent(lines.join("\n"));
      window.location.href = href;
      var status = form.querySelector("[data-status]");
      if (status) status.textContent = "Your email app should now open with the message ready to send. If it does not, write to " + to + ".";
    });
  }
})();
