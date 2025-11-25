function FormSection({ title, description, children }) {
  return (
    <section className="space-y-2">
      <div>
        <h2 className="text-base sm:text-lg font-semibold text-nutrition-darkBlue">
          {title}
        </h2>
        {description && (
          <p className="text-xs sm:text-sm text-gray-500">{description}</p>
        )}
      </div>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4 md:gap-6">
        {children}
      </div>
    </section>
  );
}

export default FormSection;