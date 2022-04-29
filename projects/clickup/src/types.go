package clickup

// ClickUp types

type User struct {
	Id                int    `json:"id"`
	Username          string `json:"username"`
	Email             string `json:"email"`
	Color             string `json:"color"`
	ProfilePictureUrl string `json:"profilePicture"`
	Initials          string `json:"initials"`
	WeekStartDay      int    `json:"week_start_day"`
	GlobalFontSupport bool   `json:"global_font_support"`
	Timezone          string `json:"timezone"`
}

type Team struct {
	Id        string `json:"id"`
	Name      string `json:"name"`
	Color     string `json:"color"`
	AvatarUrl string `json:"avatar"`
	Members   []User `json:"members"`
}

type ListStatus struct {
	Status    string `json:"status"`
	Color     string `json:"color"`
	HideLabel bool   `json:"hide_label"`
}

type List struct {
	Id         string     `json:"id"`
	Name       string     `json:"name"`
	OrderIndex int        `json:"orderindex"`
	Content    string     `json:"content"`
	Status     ListStatus `json:"status"`

	//   "priority": {
	//     "priority": "high",
	//     "color": "#f50000"
	//   },
	//   "assignee": null,
	//   "task_count": null,
	//   "due_date": "1567780450202",
	//   "due_date_time": true,
	//   "start_date": null,
	//   "start_date_time": null,
	//   "folder": {
	//     "id": "456",
	//     "name": "Folder Name",
	//     "hidden": false,
	//     "access": true
	//   },
	//   "space": {
	//     "id": "789",
	//     "name": "Space Name",
	//     "access": true
	//   },
	//   "inbound_address": "add.task.124.ac725f.31518a6a-05bb-4997-92a6-1dcfe2f527ca@tasks.clickup.com",
	//   "archived": false,
	//   "override_statuses": false,
	//   "statuses": [
	//     {
	//       "status": "to do",
	//       "orderindex": 0,
	//       "color": "#d3d3d3",
	//       "type": "open"
	//     },
	//     {
	//       "status": "complete",
	//       "orderindex": 1,
	//       "color": "#6bc950",
	//       "type": "closed"
	//     }
	//   ],
	//   "permission_level": "create"
	// }
}

type Space struct {
	// {
	//   "id": "790",
	Id string `json:"id"`

	//   "name": "Updated Space Name",
	//   "private": false,
	//   "statuses": [
	//     {
	//       "status": "to do",
	//       "type": "open",
	//       "orderindex": 0,
	//       "color": "#d3d3d3"
	//     },
	//     {
	//       "status": "complete",
	//       "type": "closed",
	//       "orderindex": 1,
	//       "color": "#6bc950"
	//     }
	//   ],
	//   "multiple_assignees": false,
	//   "features": {
	//     "due_dates": {
	//       "enabled": false,
	//       "start_date": false,
	//       "remap_due_dates": false,
	//       "remap_closed_due_date": false
	//     },
	//     "time_tracking": {
	//       "enabled": false
	//     },
	//     "tags": {
	//       "enabled": false
	//     },
	//     "time_estimates": {
	//       "enabled": false
	//     },
	//     "checklists": {
	//       "enabled": true
	//     },
	//     "custom_fields": {
	//       "enabled": true
	//     },
	//     "remap_dependencies": {
	//       "enabled": false
	//     },
	//     "dependency_warning": {
	//       "enabled": false
	//     },
	//     "portfolios": {
	//       "enabled": false
	//     }
	//   }
	// }
}
