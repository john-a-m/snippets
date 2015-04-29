;; add melpa
(when (>= emacs-major-version 24)
  (require 'package)
  (package-initialize)
  (add-to-list 'package-archives '("melpa" . "http://melpa.milkbox.net/packages/") t)
)

;; add theme
(add-to-list 'custom-theme-load-path "~/emacsthemes/")
(load-theme 'zenburn t)

;; hide useless things
(menu-bar-mode -1)
(tool-bar-mode -1)
(scroll-bar-mode -1)
