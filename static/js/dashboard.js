// Provider Dashboard Functions
function updateOrderStatus(orderId, status) {
    fetch('/api/orders/update-status/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify({
            order_id: orderId,
            status: status
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            showNotification('Order status updated successfully');
        }
    });
}

// Client Dashboard Functions
function bookService(providerId) {
    const serviceType = document.querySelector('#service-type').value;
    const pickupDate = document.querySelector('#pickup-date').value;

    fetch('/api/orders/create/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify({
            provider_id: providerId,
            service_type: serviceType,
            pickup_date: pickupDate
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            window.location.href = '/orders/' + data.order_id;
        }
    });
}

// Utility Functions
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function addNewService() {
    window.location.href = '/providers/services/add/';
}
