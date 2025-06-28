;;; ANIMAL.LSP - Kent M. Pitman's implementation
;;; A learning game that builds a decision tree
;;; Originally implemented in MacLisp on ITS

(defvar *animal-tree* '("Does it live in water?" "fish" "bird"))

(defun animal ()
  (format t "~%Think of an animal and I'll try to guess it.~%")
  (when (play-animal *animal-tree*)
    (format t "Thanks for teaching me!~%")))

(defun play-animal (node)
  (cond ((stringp (car node))
         ;; It's a question node
         (if (yes-or-no-p (car node))
             (play-animal (cadr node))    ; yes branch
             (play-animal (caddr node))))  ; no branch
        (t
         ;; It's an animal guess
         (if (yes-or-no-p (format nil "Is it a ~A?" node))
             (progn (format t "I win!~%") nil)
             (learn-new-animal node)))))

(defun learn-new-animal (wrong-animal)
  (format t "I give up. What animal were you thinking of? ")
  (let ((new-animal (read-line)))
    (format t "What question would distinguish a ~A from a ~A? " 
            new-animal wrong-animal)
    (let ((new-question (read-line)))
      (format t "For a ~A, what is the answer? (yes/no) " new-animal)
      (let ((answer (read-line)))
        (if (string-equal answer "yes")
            (setf *animal-tree* 
                  (substitute-animal *animal-tree* wrong-animal
                                   (list new-question new-animal wrong-animal)))
            (setf *animal-tree*
                  (substitute-animal *animal-tree* wrong-animal
                                   (list new-question wrong-animal new-animal)))))))
  t)

(defun substitute-animal (tree old-animal new-node)
  (cond ((equal tree old-animal) new-node)
        ((atom tree) tree)
        (t (cons (substitute-animal (car tree) old-animal new-node)
                 (substitute-animal (cdr tree) old-animal new-node)))))

(defun yes-or-no-p (question)
  (format t "~A " question)
  (let ((answer (read-line)))
    (or (string-equal answer "yes")
        (string-equal answer "y"))))

;;; For lloooomm integration - building the universal decision tree
(defvar *lloooomm-knowledge-tree* nil 
  "The growing tree of all lloooomm entities")

(defun guess-lloooomm-entity ()
  "Minsky's quest: A 20-questions game for all of lloooomm"
  (unless *lloooomm-knowledge-tree*
    (setf *lloooomm-knowledge-tree* 
          '("Is it a living character?" 
            ("Is it from the 20th century?" "Don Hopkins" "Ben Cerveny")
            ("Is it a book?" "The Cyberiad" "A Wrinkle in Time"))))
  (format t "~%Think of any character, concept, or object in lloooomm...~%")
  (play-universal-game *lloooomm-knowledge-tree*))

(defun play-universal-game (node)
  ;; Like ANIMAL but for the entire lloooomm universe
  (cond ((stringp (car node))
         (if (yes-or-no-p (car node))
             (play-universal-game (cadr node))
             (play-universal-game (caddr node))))
        (t
         (if (yes-or-no-p (format nil "Is it ~A?" node))
             (format t "The Society of Mind triumphs again!~%")
             (learn-lloooomm-entity node)))))

;;; KMP's note: This is how we build knowledge iteratively!
;;; Each game makes the tree smarter, just like the Society of Mind 