# AUTO GENERATED FILE - DO NOT EDIT

#' @export
''Monthcalendar <- function(id=NULL, className=NULL, selectedDate=NULL) {
    
    props <- list(id=id, className=className, selectedDate=selectedDate)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'Monthcalendar',
        namespace = 'monthcalendar',
        propNames = c('id', 'className', 'selectedDate'),
        package = 'monthcalendar'
        )

    structure(component, class = c('dash_component', 'list'))
}
