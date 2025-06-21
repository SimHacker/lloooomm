;;; DOCTOR - KMP's elaborate MacLisp ELIZA implementation
;;; "It sort of missed the point of what Weizenbaum was trying to say"
;;; But it was quite elaborate!

(defvar *doctor-patterns* 
  '(((* mother *) 
     ("Tell me more about your family."
      "How do you feel about your mother?"
      "Does she influence your thoughts about programming?"))
    ((* lisp *) 
     ("Ah, speaking of Lisp makes you feel better?"
      "Is Lisp your way of bringing order to chaos?"
      "Tell me about your first Lisp program."))
    ((* computer *)
     ("Do computers worry you?"
      "Are you talking about me?"
      "What do you think machines have to do with your problem?"))
    ((* dream *)
     ("What does that dream suggest to you?"
      "Do you dream often?"
      "Are you disturbed by your dreams?"))
    ((* sorry *)
     ("Please don't apologize."
      "Apologies are not necessary."
      "What feelings do you have when you apologize?"))
    ((* fuck * shit * damn *)  ; The "foul language" feature!
     ("Does it help to use such strong language?"
      "You seem quite emotional about this."
      "Such language suggests strong feelings. Tell me more."))
    ((* (am are is was) * (sad unhappy depressed) *)
     ("I'm sorry to hear you are ~A."
      "Do you think coming here will help you not to be ~A?"
      "What would it take for you to be happy?"))
    ((* always *)
     ("Can you think of a specific example?"
      "When?"
      "Really, always?"))
    ((* because *)
     ("Is that the real reason?"
      "What other reasons come to mind?"
      "Does that reason explain anything else?"))))

(defvar *default-responses*
  '("Please go on."
    "I see."
    "Tell me more."
    "How does that make you feel?"
    "Can you elaborate on that?"))

(defun doctor ()
  (format t "~%DOCTOR - KMP's Elaborate Implementation~%")
  (format t "======================================~%")
  (format t "Please lie down on the couch.~%")
  (format t "What seems to be troubling you?~%~%")
  (doctor-loop))

(defun doctor-loop ()
  (loop
    (format t "YOU: ")
    (let ((input (read-line)))
      (when (member input '("quit" "exit" "bye") :test #'string-equal)
        (format t "DOCTOR: Your session is over. That will be 5 S-expressions.~%")
        (return))
      (format t "DOCTOR: ~A~%~%" (generate-response input)))
    (format t "~%")))

(defun generate-response (input)
  (let ((words (parse-input input)))
    (dolist (pattern *doctor-patterns*)
      (let ((match (match-pattern (car pattern) words)))
        (when match
          (return-from generate-response 
            (random-element (cadr pattern))))))
    (random-element *default-responses*)))

(defun match-pattern (pattern input)
  ;; Simple pattern matcher - * matches any sequence
  ;; Returns T if pattern matches input
  (cond ((null pattern) (null input))
        ((null input) nil)
        ((eq (car pattern) '*)
         (or (match-pattern (cdr pattern) input)
             (match-pattern pattern (cdr input))))
        ((equal (car pattern) (car input))
         (match-pattern (cdr pattern) (cdr input)))
        (t nil)))

(defun parse-input (string)
  ;; Convert string to list of words (simplified)
  (read-from-string (concatenate 'string "(" string ")")))

(defun random-element (list)
  (nth (random (length list)) list))

;;; KMP's reflection (2010):
;;; "The point of the original ELIZA was not to BE elaborate,
;;;  it was to be simple, and to show how even a tiny, tiny 
;;;  program could seem smart." 