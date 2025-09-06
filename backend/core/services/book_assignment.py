"""
Service module for book assignment logic.
Handles computing unread books, selecting next books, and updating group book assignments.
"""

from django.apps import apps


class BookSourceNotConfigured(Exception):
    """Raised when no book provider is configured for an archetype."""

    pass


def get_unread_books(group):
    """
    Compute unread books for a group based on group.archetype, group.books_read (completed),
    and group.current_book (currently assigned).

    Args:
        group: Group instance

    Returns:
        QuerySet of unread Book instances for the group's archetype
    """
    Book = apps.get_model("core", "Book")
    read_book_ids = group.books_read.values_list("id", flat=True)

    # Exclude completed books
    unread_books = Book.objects.filter(archetype=group.archetype).exclude(
        id__in=read_book_ids
    )

    # Exclude current book if present
    if group.current_book_id:
        unread_books = unread_books.exclude(id=group.current_book_id)

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
        return unread_books.order_by("id").first()
    else:
        return fetch_new_book(group.archetype)


def fetch_new_book(archetype):
    """
    Placeholder function to fetch a new book for an archetype.
    TODO: Implement external API call to fetch new book recommendations.

    Args:
        archetype: Archetype instance

    Returns:
        Book instance (currently raises BookSourceNotConfigured)
    """
    # Placeholder: raise until external API is implemented
    raise BookSourceNotConfigured(
        "No book provider configured. Implement external book fetch for this archetype."
    )


def assign_next_book_to_group(group):
    """
    Assign the next book to a group.
    Updates group.current_book and saves. Does NOT add to books_read (completed books).

    Args:
        group: Group instance

    Returns:
        The assigned Book instance
    """
    next_book = choose_next_book(group)

    group.current_book = next_book
    group.save()

    return next_book


def mark_current_book_finished(group):
    """
    Mark the current book as finished for a group.
    Moves the current book to books_read (completed) and clears current_book.

    Args:
        group: Group instance

    Returns:
        The finished Book instance, or None if no current book
    """
    if not group.current_book:
        return None

    finished_book = group.current_book
    group.books_read.add(finished_book)
    group.current_book = None
    group.save()

    return finished_book
