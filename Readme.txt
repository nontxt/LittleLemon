admin/  -- Admin site
restaurant/ -- Restaurant index page
restaurant/menu/ -- List of Menu items or create a new instance
restaurant/menu/<int:pk>/ -- Retrieve/Edit/Delete a Menu item
restaurant/bookings/tables -- CRUD operations for Bookings (only for authenticated)
auth/  -- Djoser urls
auth/users/ -- Create a new User
auth/token/login/ -- Create a new API token from valid credentials (provided by the Djoser)
auth/token/logout/  -- Destroy the API token
api-token-auth/ -- Create a new API token from valid credentials (provided by the DRF)
