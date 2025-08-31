"""
Service module for book assignment logic.
Handles computing unread books, selecting next books, and updating group book assignments.
"""
from django.apps import apps


def get_unread_books(group):
    """
    Compute unread books for a group based on group.archetype and group.books_read.
    
    Args:
        group: Group instance
        
    Returns:
        QuerySet of unread Book instances for the group's archetype
    """
    Book = apps.get_model('core', 'Book')
    read_books = group.books_read.all()
    unread_books = Book.objects.filter(
        archetype=group.archetype
    ).exclude(
        id__in=read_books.values_list('id', flat=True)
    )
    return unread_books


def choose_next_book(group):
    """
    Choose the next book for a group (unread first).
    If no unread books exist, fetches a new book via fetch_new_book.
    
    Args:
        group: Group instance
        
    Returns:
        Book instance to be assigned next
    """
    unread_books = get_unread_books(group)
    
    if unread_books.exists():
        return unread_books.first()
    else:
        return fetch_new_book(group.archetype)


def fetch_new_book(archetype):
    """
    Placeholder function to fetch a new book for an archetype.
    TODO: Implement external API call to fetch new book recommendations.
    
    Args:
        archetype: Archetype instance
        
    Returns:
        Book instance (currently raises NotImplementedError)
    """
    # Placeholder: raise NotImplementedError until external API is implemented
    raise NotImplementedError(
        "fetch_new_book is not yet implemented. "
        "External API integration required."
    )


def assign_next_book_to_group(group):
    """
    Assign the next book to a group.
    Updates group.current_book, adds to group.books_read, and saves.
    
    Args:
        group: Group instance
        
    Returns:
        The assigned Book instance
    """
    next_book = choose_next_book(group)
    
    group.current_book = next_book
    group.books_read.add(next_book)
    group.save()
    
    return next_book
