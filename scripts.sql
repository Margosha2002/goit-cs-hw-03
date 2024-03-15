-- Отримати всі завдання певного користувача.
-- user_id = 1
SELECT * FROM tasks LEFT JOIN status ON tasks.status_id = status.id WHERE user_id = 101

-- Вибрати завдання за певним статусом
-- status = new
SELECT * FROM tasks LEFT JOIN status ON tasks.status_id = status.id WHERE status.name = 'new'

-- Оновити статус конкретного завдання.
-- task_id = 1
-- new_status = 'in progress'
UPDATE 
	tasks 
SET status_id = s.id 
	FROM tasks AS t 
		INNER JOIN status AS s ON s.name = 'in progress' AND t.id = 1 
WHERE tasks.id = 1

-- Отримати список користувачів, які не мають жодного завдання.
SELECT * FROM users AS u WHERE u.id NOT IN (SELECT t.user_id FROM tasks AS t)

-- Додати нове завдання для конкретного користувача
INSERT INTO tasks(title, description, status_id, user_id) VALUES ('title', 'description', 1, 2)

-- Отримати всі завдання, які ще не завершено.
SELECT * FROM tasks AS t LEFT JOIN status AS s ON t.status_id = s.id WHERE s.name != 'completed'

-- Видалити конкретне завдання.
DELETE FROM tasks AS t WHERE t.id = 405

-- Знайти користувачів з певною електронною поштою.
SELECT * FROM users AS u WHERE u.email LIKE '%email%'

-- Оновити ім'я користувача.
UPDATE users SET fullname = 'new name' WHERE id = 301

-- Отримати кількість завдань для кожного статусу.
SELECT s.id, s.name, COUNT(t.id) AS "tasksCount" FROM tasks AS t LEFT JOIN status AS s ON t.status_id = s.id GROUP BY s.id, s.name

-- Отримати завдання, які призначені користувачам з певною доменною частиною електронної пошти.
SELECT * FROM tasks AS t LEFT JOIN users AS u ON u.id = t.user_id WHERE u.email LIKE '%@example.com'

-- Отримати список завдань, що не мають опису.
SELECT * FROM tasks WHERE description IS NULL

-- Вибрати користувачів та їхні завдання, які є у статусі 'in progress'
SELECT
	u.id AS "userId",
	u.fullname AS "userName",
    u.email AS "userEmail",
	jsonb_agg(
		jsonb_build_object(
			'id', t.id,
			'title', t.title,
			'description', t.description,
			'status', s.name
		)
	) AS "userTasks"
FROM users AS u 
	INNER JOIN tasks AS t ON u.id = t.user_id 
	LEFT JOIN status AS s ON t.status_id = s.id
WHERE s.name = 'in progress'
GROUP BY u.id, u.fullname, u.email

-- Отримати користувачів та кількість їхніх завдань.
SELECT
	u.id,
	u.fullname,
	u.email,
	COUNT(t.id) AS "tasksCount"
FROM users AS u
	LEFT JOIN tasks AS t ON u.id = t.user_id
GROUP BY u.id, u.fullname, u.email
